# INTEL-UNNATI-PS-11-SUBMISSION

# DETAILS
NAME - N PALANI KARTHIK

EMAIL - palanikarthik.n2022@vitstudent.ac.in

PROBLEM STATEMENT - INTEL PRODUCTS SENTIMENT ANALYSIS FROM ONLINE REVIEWS (PS11)

DATASET SIZE - 20000 records from various ecommerce site (CUSTOMER BASED)

DATASET NAME - conclusions_updated (Cleaned dataset with predicted sentiment in 1. MODEL WITH MAIN SCRIPT folder)


# IMP LINKS
webiste link - https://intel-karthiknp-sentimental-analysis.streamlit.app/

github link - https://github.com/palkar22/INTEL-UNNATI-PS-11-SUBMISSION

video link - 

full dataset link - https://huggingface.co/datasets/palkar22/20000_data_points_intel
 
finetuning dataset link - https://huggingface.co/datasets/palkar22/intel_unnati    


----------------------


1) Run the Sentimental_analysis_intel.ipynb in 1. MODEL WITH MAIN SCRIPT folder
   
2) Make sure to put test_actual_reviews.xlsx, Intel reviews 20000 records final.xlsx, conclusions_updated.xlsx in working directory before running code.
   
3)run LLM FINETUNING AND MODEL BUILDING section in Sentimental_analysis_intel.ipynb first before others if finetuned llama3 model is to be saved first

-Type streamlit run intel_sentiment_analyzer.py in D:\intel\3. intel-karthik-website for running website locally with replicate api key otherwise use the link directly on https://intel-karthiknp-sentimental-analysis.streamlit.app/

-All output images are on 2. OUTPUT IMAGES folder

-Unzip the adapter_model file as GitHub allows max 100MB file and extract it from the llama3 for exact model file.
Do not unzip if running the code Sentimental_analysis_intel.ipynb.

-The report of the project is available in REPORT PDF

-Scrapping details are available under Scrapping dump folder

Kindly refer to the YOUTUBE VIDEO LINK FOR IMPLEMENTATION (https://youtu.be/i_1e732WVyQ?feature=shared)  incase of any doubt.

ABSTRACT/WORKING OF PROJECT -

 This project employs advanced NLP techniques for sentiment analysis of Intel product reviews
 by leveraging the Llama2 language model fine-tuned with the Ollama API. The process begins
 with data preprocessing, where customer reviews are tokenized into smaller units called
 tokens. This step is essential for effectively handling and analyzing the text, capturing the
 nuances and context of each review.

 Once tokenized, the reviews are fed into Llama2, a robust language model known for its
 accuracy in understanding and generating human-like text. Fine-tuning Llama2 involves
 training the pre-trained model specifically on a dataset of Intel product reviews. This allows
 the model to learn the specific language patterns, sentiments, and terminologies associated
 with these products, enhancing its ability to discern subtle differences in sentiment and
 provide more accurate predictions. The Ollama API facilitates this process by offering a
 seamless interface to train, evaluate, and deploy the model.

 After fine-tuning, the LLM can analyze new customer reviews and classify them into positive,
 negative, or neutral sentiments. This classification gives Intel a granular understanding of
 customer opinions, enabling the identification of trends and patterns in consumer feedback.
 For example, analyzing whether the number of positive reviews has increased over time can
 provide insights into the effectiveness of recent product improvements or marketing
 campaigns.

 In summary, this project leverages the power of Llama2 and the Ollama API to perform
 sophisticated sentiment analysis on Intel product reviews. By fine-tuning the model with
 specific data, we ensure high accuracy and relevance in sentiment classification. The resulting
 insights provide Intel with a deeper understanding of customer satisfaction and areas for
 improvement, ultimately guiding the company towards better products and enhanced
 customer experiences.


