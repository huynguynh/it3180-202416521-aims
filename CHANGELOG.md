# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.1] - 2026-11-06

### Fixed
- Make `search_by_title()` case-insensitive (#21).

## [1.0.0] - 2026-11-06

### Added
- `Cart.print_cart()` to display cart items and handle empty cart state.
- `search_by_title()` in `aims/search.py` to search DVDs by title keyword.
- `Cart.total_cost_with_discount()` with discount percentage validation.
- Vietnamese notification message when adding a DVD to cart.
- Unit test suite (`tests/test_cart.py`) using `unittest`.
- Project documentation (`docs/use-case.md`, pull request template, Lab 01–03 discussion answers).

### Fixed
- Reject adding the 21st DVD when the cart reaches `MAX_NUMBERS_ORDERED = 20` (#8).
- Return discounted total instead of discount amount in `total_cost_with_discount()` and validate `0 <= percent <= 100`.
