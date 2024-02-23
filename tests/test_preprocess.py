"""Tests for `preprocess` package."""
# pylint: disable=redefined-outer-name

import pytest

from kedatatext.preprocessing import clean_sentence_indonesia, clean_sentences_indonesia


def test_clean_sentence_indonesia():
    text = "RT @canggih: Mereka lihat ini: https://example.com"
    cleaned_text = clean_sentence_indonesia(text)
    assert cleaned_text == "lihat"


def test_clean_sentence_indonesia_no_stemming():
    text = "RT @canggih: Mereka lihat ini: https://example.com"
    cleaned_text = clean_sentence_indonesia(text, use_stemming=False)
    assert cleaned_text == "lihat"


def test_clean_sentence_indonesia_no_remove_stopwords():
    text = "RT @canggih: Mereka lihat ini: https://example.com"
    cleaned_text = clean_sentence_indonesia(text, remove_stopwords=False)
    assert cleaned_text == "mereka lihat ini"


def test_clean_sentence_indonesia_no_remove_retweet():
    text = "RT @canggih: Mereka lihat ini: https://example.com"
    cleaned_text = clean_sentence_indonesia(text, remove_retweet=False)
    assert cleaned_text == "rt lihat"


def test_clean_sentence_indonesia_no_remove_urls():
    text = "RT @canggih: Mereka lihat ini: https://example.com"
    cleaned_text = clean_sentence_indonesia(text, remove_urls=False)
    assert cleaned_text == "lihat httpsexamplecom"


def test_clean_sentence_indonesia_no_remove_mentions():
    text = "RT @canggih: Mereka lihat ini: https://example.com"
    cleaned_text = clean_sentence_indonesia(text, remove_mentions=False)
    assert cleaned_text == "canggih lihat"


def test_clean_sentence_indonesia_no_remove_hashtags():
    text = "RT @canggih: Mereka lihat ini: https://example.com"
    cleaned_text = clean_sentence_indonesia(text, remove_hashtags=False)
    assert cleaned_text == "lihat"


def test_clean_sentence_indonesia_no_remove_numbers():
    text = "RT @canggih: Mereka lihat ini: https://example.com"
    cleaned_text = clean_sentence_indonesia(text, remove_numbers=False)
    assert cleaned_text == "lihat"


def test_clean_sentence_indonesia_no_remove_extra_ws():
    text = "RT @canggih: Mereka lihat ini: https://example.com"
    cleaned_text = clean_sentence_indonesia(text, remove_extra_whitespace=False)
    assert cleaned_text == "lihat"


def test_clean_sentence_indonesia_no_remove_punkt():
    text = "RT @canggih: Mereka lihat ini: https://example.com"
    cleaned_text = clean_sentence_indonesia(text, remove_punctuation=False)
    assert cleaned_text == "lihat"


def test_clean_sentences_indonesia():
    text = ["RT @canggih: Mereka lihat ini: https://example.com"]
    cleaned_text = clean_sentences_indonesia(text)
    assert cleaned_text == ["lihat"]
