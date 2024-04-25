#use a python image as base
FROM python
#set the working directory inside the container
WORKDIR /app


#install NLTK
RUN pip install --no-cache-dir nltk

# Copy your Python file into the container
COPY . .

# run the Python script
CMD ["python", "python.py"]
