.PHONY: setup clean test test-lru test-array test-substring lint type-check format check-all

# Variables
PYTHON := python
VENV := venv
BIN := $(VENV)/bin
SRC_DIR := src
TEST_DIR := tests

help:
	@echo "Available commands:"
	@echo "  make setup         - Create virtual environment and install dependencies"
	@echo "  make clean        - Remove virtual environment and cache files"
	@echo " "
	@echo "  make test         - Run all tests"
	@echo "  make test-lru     - Run LRU Cache tests"
	@echo "  make test-array   - Run Array Threshold tests"
	@echo "  make test-substring - Run Longest Substring tests"
	@echo " "
	@echo "  make lint         - Run pylint"
	@echo "  make type-check   - Run mypy type checking"
	@echo "  make format       - Format code with black"
	@echo "  make check-all    - Run all checks (lint, type-check, test)"

setup:
	$(PYTHON) -m venv $(VENV)
	$(BIN)/pip install --upgrade pip
	$(BIN)/pip install -r requirements.txt

clean:
	rm -rf $(VENV)
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf .mypy_cache
	rm -rf **/__pycache__


test:
	PYTHONPATH=. $(BIN)/pytest $(TEST_DIR) -v

test-lru:
	PYTHONPATH=. $(BIN)/pytest $(TEST_DIR)/test_lru_cache.py -v

test-array:
	PYTHONPATH=. $(BIN)/pytest $(TEST_DIR)/test_array_threshold.py -v

test-substring:
	PYTHONPATH=. $(BIN)/pytest $(TEST_DIR)/test_longest_substring.py -v

lint:
	$(BIN)/pylint $(SRC_DIR) $(TEST_DIR)

type-check:
	$(BIN)/mypy $(SRC_DIR) $(TEST_DIR)

format:
	$(BIN)/black $(SRC_DIR) $(TEST_DIR)

check-all: lint type-check test 

test-junit:
	mkdir -p test-reports
	PYTHONPATH=. $(BIN)/pytest $(TEST_DIR)/test_lru_cache.py -v --junitxml=test-reports/test-lru.xml || true
	PYTHONPATH=. $(BIN)/pytest $(TEST_DIR)/test_array_threshold.py -v --junitxml=test-reports/test-array.xml || true 
	PYTHONPATH=. $(BIN)/pytest $(TEST_DIR)/test_longest_substring.py -v --junitxml=test-reports/test-substring.xml || true