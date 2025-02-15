import pandas as pd
import numpy as np
from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
from sentence_transformers import SentenceTransformer
from langchain_chroma import Chroma

#from gradio import 
import gradio as gr

load_dotenv()

books = pd.read_csv("books_with_emotion.csv")

books["large_thuumbnail"] =books["thumbnail"] + "&fife=w888"
books['large_thuumbnail']= np.where(
    books['large_thuumbnail'].isna(),
    "cover-not-found.jpg",
    books['large_thuumbnail']
)


# Build Vector Database:
raw_documents = TextLoader("/Users/chetu/Learning/LLM/BookRecommender/tagged_description.txt").load()
text_splitter = CharacterTextSplitter(chunk_size=0, chunk_overlap=0, separator="\n")  
documents = text_splitter.split_documents(raw_documents)
model = SentenceTransformer('all-MiniLM-L6-v2') 
embedding = SentenceTransformerEmbeddings(model_name='all-MiniLM-L6-v2') 
db_books = Chroma.from_documents(
    documents=documents,
    embedding=embedding
)

def retrieve_semantics_recommendation(
        query : str,
        category: str,
        tone: None,
        initial_top_k: int=50,
        final_top_k: int=16
        ) -> pd.DataFrame:
    

    recs = db_books.similarity_search(query, k=initial_top_k)
    books_list = [int(rec.page_content.strip('"').split()[0]) for rec in recs]
    print(books_list)
    books_recs = books[books["isbn13"].isna(books_list)].head(final_top_k)


    #Drop down on dashboard
    if category != 'All':
        book_recs = book_recs[book_recs["simpple_categories"] ==category].head(final_top_k)
    else:
        book_recs = book_recs.head(final_top_k)

    if tone == "Happy":
        book_recs.sort_values(by="joy", ascending=False, inplace=True)
    elif tone == "Suprising":
        book_recs.sort_values(by="suprise", ascending=False, inplace=True)
    elif tone == "Suspenseful":
        book_recs.sort_values(by="fear", ascending=False, inplace=True)
    elif tone == "Sad":
        book_recs.sort_values(by="sad", ascending=False, inplace=True)

    return books_recs


def recommend_books(
        query: str,
        category: str,
        tone: str
        ):
    recommendations = retrieve_semantics_recommendation(query, category, tone)

    results = []

    for _, raw in recommendations.iterrows():
        description =raw["description"]
        truncated_desc_split = description.split()
        truncated_description = " ".join(truncated_desc_split[:30])+"...."


        author_split = raw["authors"].split(";")

        if len(author_split) ==2:
            author_str = f"{author_split[0]} and {author_split[1]}"
        
        elif len(author_split) > 2:
            author_str = f'{", ".join(author_split[:-1])} and {author_split[-1]}'
        else:
            author_str =raw["authors"]
        
        caption = f"{raw['title']} by {author_str}: {truncated_description}"

        results.append((raw["large_thumbnail"], caption))

    return results

catgories = ["All"] + sorted(books["simpple_categories"].unique())
tones = ["All"] + ["Happy", "Suprising","Suspenseful","Angry","Sad",]

with gr.Blocks(theme = gr.themes.Glass()) as dashboard:
    gr.Markdown("# Semnatic Book Recommendation")


    with gr.Row():
        user_query = gr.Textbox(label = "Please enter a description for a book: ",
                                placeholder = "e.g.. A story about the adventorous journey..")
        
        category_dropdown = gr.Dropdown(choices =catgories, label = "Select a category:", value="All")
        tone_dropdown = gr.Dropdown(choices =tones, label = "Select a emotional tone:", value="All")
        submit_button = gr.Button("find Recommedations")

    
    gr.Markdown("## Recomendations")
    output = gr.Gallery(label ="Recommended Books", columns=8, rows=2)

    submit_button.click(fn=recommend_books,
                        inputs = [user_query, category_dropdown, tone_dropdown],
                        outputs=output)

if __name__ == '__main__':

    dashboard.launch()