import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Download the stopwords package and punkt tokenizer model
nltk.download('stopwords')
nltk.download('punkt')

# Get the list of English stop words
stop_words = set(stopwords.words('english'))


# Example text (you can replace this with your own text)
text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

# Tokenize the text (split into words)
words = word_tokenize(text)

# Remove stop words
filtered_words = [word for word in words if word.lower() not in stop_words]

# Join the filtered words back into a string
filtered_text = ' '.join(filtered_words)

# Create word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(filtered_text)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
