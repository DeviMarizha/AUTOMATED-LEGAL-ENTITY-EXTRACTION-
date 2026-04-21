START

INITIALIZE Streamlit application

LOAD trained Legal-BERT model configuration
CHECK if model files exist
IF model not found:
    DISPLAY error message
    STOP execution

DISPLAY file upload option to user

IF user uploads document:
    READ file (TXT / PDF / DOCX)
    EXTRACT text content

    DISPLAY extracted text preview

    IF user clicks "Extract Entities":
        
        PREPROCESS text
            - Clean text
            - Normalize format
            - Tokenize words
        
        APPLY NER Model
            FOR each token in text:
                PREDICT entity label (BIO tagging)
        
        APPLY Semantic Filtering
            FOR each predicted entity:
                CALCULATE similarity score
                IF similarity > threshold:
                    ACCEPT entity
                ELSE:
                    REJECT entity
        
        STORE extracted entities
            - Entity name
            - Label type
            - Start & end position
            - Confidence score
        
        DISPLAY RESULTS:
            - Highlighted text with entities
            - Entity table (word, label, score)
            - Statistical charts (entity distribution)
            - Summary of document

END