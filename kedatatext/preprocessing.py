import re
import string
from typing import List

from nltk.corpus import stopwords  # type: ignore
from nltk.tokenize import word_tokenize  # type: ignore
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory  # type: ignore

factory = StemmerFactory()
stemmer = factory.create_stemmer()


def clean_sentence_indonesia(
    text: str,
    to_lower: bool = True,
    use_stemming: bool = True,
    remove_stopwords: bool = True,
    remove_punctuation: bool = True,
    remove_numbers: bool = True,
    remove_urls: bool = True,
    remove_mentions: bool = True,
    remove_hashtags: bool = True,
    remove_retweet: bool = True,
    remove_extra_whitespace: bool = True,
) -> str:
    """
    Cleans a text sentence by applying various preprocessing techniques.

    Args:
        text (str): The input text sentence.
        to_lower (bool, optional): Whether to convert the text to lowercase. Defaults to True.
        use_stemming (bool, optional): Whether to apply stemming to words. Defaults to True.
        remove_stopwords (bool, optional): Whether to remove Indonesian stop words. Defaults to True.
        remove_punctuation (bool, optional): Whether to remove punctuation characters. Defaults to True.
        remove_numbers (bool, optional): Whether to remove numeric characters. Defaults to True.
        remove_urls (bool, optional): Whether to remove URLs. Defaults to True.
        remove_mentions (bool, optional): Whether to remove mentions (starting with "@"). Defaults to True.
        remove_hashtags (bool, optional): Whether to remove hashtags (starting with "#"). Defaults to True.
        remove_retweet (bool, optional): Whether to remove "RT" at the beginning of retweets. Defaults to True.
        remove_extra_whitespace (bool, optional): Whether to remove extra whitespace characters. Defaults to True.

    Returns:
        str: The cleaned text sentence.

    Examples:
        >>> text = "RT @canggih: Mereka lihat ini: https://example.com"
        >>> cleaned_text = clean_sentence_indonesia(text, remove_urls=True, remove_mentions=True, remove_hashtags=True)
        >>> print(cleaned_text)
        mereka lihat ini

    Notes:
        - This function uses the `Sastrawi` library for stemming.
        - Consider adjusting the parameters based on your specific requirements.
    """

    # Remove RT
    if remove_retweet:
        if text.startswith("RT "):
            text = text[3:].strip()

    # Remove URLs
    if remove_urls:
        text = re.sub(r"http\S+", "", text)

    # Remove mentions
    if remove_mentions:
        text = re.sub("@[A-Za-z0-9]+", "", text)

    # Remove hashtags
    if remove_hashtags:
        text = re.sub("#", "", text)

    # Remove numbers
    if remove_numbers:
        text = re.sub(r"\d+", "", text)

    # Convert to lowercase
    if to_lower:
        text = text.lower()

    # Remove extra whitespace
    if remove_extra_whitespace:
        text = " ".join(text.split())

    # Remove punctuation
    if remove_punctuation:
        text = text.translate(str.maketrans("", "", string.punctuation))

    # Remove stop words
    if remove_stopwords:
        stop_words = set(stopwords.words("indonesian"))
        word_tokens = word_tokenize(text)
        filtered_sentence = [word for word in word_tokens if word not in stop_words]
        text = " ".join(filtered_sentence)

    # Stemming
    if use_stemming:
        text = stemmer.stem(text)

    return text


def clean_sentences_indonesia(
    list_of_texts: List[str],
    to_lower: bool = True,
    use_stemming: bool = True,
    remove_stopwords: bool = True,
    remove_punctuation: bool = True,
    remove_numbers: bool = True,
    remove_urls: bool = True,
    remove_mentions: bool = True,
    remove_hashtags: bool = True,
    remove_retweet: bool = True,
    remove_extra_whitespace: bool = True,
) -> List[str]:
    """
    Cleans a list of text sentences by applying various preprocessing techniques.

    Args:
        list_of_texts (List[str]): A list of input text sentences.
        to_lower (bool, optional): Whether to convert the text to lowercase. Defaults to True.
        use_stemming (bool, optional): Whether to apply stemming to words. Defaults to True.
        remove_stopwords (bool, optional): Whether to remove Indonesian stop words. Defaults to True.
        remove_punctuation (bool, optional): Whether to remove punctuation characters. Defaults to True.
        remove_numbers (bool, optional): Whether to remove numeric characters. Defaults to True.
        remove_urls (bool, optional): Whether to remove URLs. Defaults to True.
        remove_mentions (bool, optional): Whether to remove mentions (starting with "@"). Defaults to True.
        remove_hashtags (bool, optional): Whether to remove hashtags (starting with "#"). Defaults to True.
        remove_retweet (bool, optional): Whether to remove "RT" at the beginning of retweets. Defaults to True.
        remove_extra_whitespace (bool, optional): Whether to remove extra whitespace characters. Defaults to True.

    Returns:
        List[str]: A list of cleaned text sentences.

    Examples:
        >>> list_of_texts = ["RT @canggih: Mereka lihat ini: https://example.com", "Halo 123!"]
        >>> cleaned_texts = clean_sentences_indonesia(list_of_texts)
        >>> print(cleaned_texts)
        ['mereka lihat ini', 'halo']
    """
    return [
        clean_sentence_indonesia(
            text,
            to_lower,
            use_stemming,
            remove_stopwords,
            remove_punctuation,
            remove_numbers,
            remove_urls,
            remove_mentions,
            remove_hashtags,
            remove_retweet,
            remove_extra_whitespace,
        )
        for text in list_of_texts
    ]
