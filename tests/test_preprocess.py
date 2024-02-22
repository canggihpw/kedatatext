"""Tests for `preprocess` package."""

from kedatatext.preprocessing import CleaningParams, clean_sentences_indonesia


def test_clean_sentence_indonesia():
    """Function to test the cleaning of texts using a list of texts and cleaning parameters."""

    list_of_texts = [
        "RT @user: Check out this link: https://example.com",
        "Hello 123 world!",
    ]
    params = CleaningParams()

    cleaned_texts = clean_sentences_indonesia(list_of_texts, params)
    assert cleaned_texts
