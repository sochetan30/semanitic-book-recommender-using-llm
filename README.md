Got it! Here's an updated version of the README with a focus on **book recommendation** using semantic search and category filtering:

---

# Book Recommendation System Using Semantic Search

This project leverages the **7K Books with Metadata** dataset from Kaggle to build a **book recommendation system**. The system uses **semantic search** to recommend books based on the meaning behind user queries and filters the results based on categories such as **Fiction**, **Non-Fiction**, **Science Fiction**, **Biography**, and more. Built using Python, large language models (LLMs), and libraries like Gradio and Huggingface, this system provides an easy-to-use, interactive interface for book discovery and recommendations.

### Project Overview
The **7K Books with Metadata** dataset contains detailed information on over 7,000 books, including titles, authors, genres, publication years, and more. This project aims to recommend books based on the user's preferences using a **semantic search** approach that understands the context and intent of the user’s query. Additionally, users can filter book recommendations by category (such as Fiction, Non-Fiction, Mystery, and so on) to make their search more specific.

### Key Features:
- **Semantic Book Recommendation**: Recommends books based on the meaning behind user queries rather than simple keyword matching. The model leverages **embeddings** and a **pre-trained language model** to understand the user's intent.
- **Category Filtering**: Users can filter book recommendations by categories such as **Fiction**, **Non-Fiction**, **Science Fiction**, **Biography**, **Fantasy**, and others.
- **Interactive Web Interface**: Built with Gradio, the web app offers an intuitive, easy-to-use interface that allows users to interact with the recommendation system.
- **Natural Language Querying**: Users can type in natural language queries like:
  - "Recommend me books like 'The Hobbit'."
  - "Show me books in the Mystery category."
  - "Find me books by Agatha Christie."
  - "Suggest books on climate change."

### Technologies Used:
- **Python**: The core programming language used for data processing.
- **Kaggle Dataset**: The **7K Books with Metadata** dataset provides the base book information used in the recommendation system.
- **Huggingface Transformers**: Used to generate **embeddings** for semantic search and enhance recommendations through advanced NLP techniques.
- **Gradio**: A Python library to create the interactive web interface for users to interact with the book recommendation system.
- **Pandas**: Used for preprocessing and manipulating the dataset to prepare it for recommendation queries.

### Installation & Setup:
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/book-recommendation-system.git
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python gradio_dashboard.py
   ```

### Usage:
Once the application is up and running, the user can:
- Input natural language queries such as "Recommend me books on space exploration" or "Books by George Orwell."
- Filter recommendations by categories such as **Fiction**, **Non-Fiction**, **Biography**, **Romance**, **Fantasy**, etc.
- Get relevant book suggestions based on semantic understanding, not just keyword matching.
- Click on book titles to get more details, such as summaries, author information, and publication year.

### Example Queries:
- "Recommend me books about time travel."
- "Show me Fiction books similar to 'Harry Potter'."
- "Find books in the Mystery category."
- "Give me a list of books on psychology."

---
This version emphasizes the **book recommendation** aspect, making it clear that the system suggests books based on user input, incorporates **semantic search**, and allows users to filter by categories. It also highlights the technologies used to build the recommendation engine.