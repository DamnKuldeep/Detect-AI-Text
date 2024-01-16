# Detect-AI-Text
Welcome to the "LLM-Detect AI Text" project! In this repository, we present solution for detecting AI-generated text using DistilBERT by fine tuning the model.

## Working
1. Dataset:

   First we collected our dataset by merging different datasets from kaggle because we need to have a balanced dataset which contains sufficient number of examples of both Human and AI generated texts.
   Here are the links to datasets we used for this purpose. We removed the duplicate entries after merging the datasets.
   <ul>
     <li>https://www.kaggle.com/c/llm-detect-ai-generated-text</li>
     <li>https://www.kaggle.com/datasets/etiennekaiser/gemini-pro-llm-daigtdataset</li>
     <li>https://www.kaggle.com/datasets/dsluciano/daigt-one-place-all-data</li>
     <li>https://www.kaggle.com/datasets/jdragonxherrera/augmented-data-forllm-detect-ai-generated-text</li>
   </ul>


2. Preprocessing:

   KeyBERT:-
    We used KeyBERT model to extract the keywords from the text on the basis of their importance with the context of the text. This reduced the length of text because we took 70% of words which reduced the training time and also since the training examples got arranged from higher importance of word to lower in sequence, this made it easy for the model to differentiate between Human and AI generated texts because in both cases different words hold different importances.

   Tokenizer:-
    After getting the extracted keyword text data from keybert, we passed it to the distilberttokenizerfast, which mapped the text to the vocabulary and converted the text data to numeric data by padding and truncating it to max length of 512 tokens, which is easier to process and compatible with Distilbert model. 



3. Training:

   Then we loaded the pretrained DistilBert model and trained it on our training dataset, for that purpose we used the GPU provided by kaggle with a limit of 30 hours per week.
   and also validated on the splitted test dataset, and got a very good accuracy of 99.11% on it, which showed our model is good to go.

4. Deploying:

   Then we deployed the model on a website and rendered the website using flask.


## Installation and Site Testing

1. Clone the repository:
   ```sh
   git clone https://github.com/DamnKuldeep/Detect-AI-Text.git
   cd Detect-AI-Text
   ```

2. Get Large Files:
   ```sh
   git lfs fetch
   git pull
   ```

3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Run the Website:
   ```sh
   python app.py
   ```

5. Access the AI Text Detector Website:
   
  Open your web browser and go to the link provided in the terminal (e.g., http://127.0.0.1:5000).

  Paste the text and check result.
