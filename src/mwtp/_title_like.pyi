import re
from typing import ClassVar, Optional, overload, Self, SupportsIndex


class TitleLike:
	'''
	A thin wrapper around a string, providing some convenient methods
	for formatting and validating it.

	Meant to be used internally.
	'''
	
	_whitespace_char_codes: ClassVar[tuple[int]]
	_unicode_bidi_char_codes: ClassVar[tuple[int]]
	
	_whitespace_series: ClassVar[re.Pattern[str]]
	_unicode_bidi_marks: ClassVar[re.Pattern[str]]
	
	_first_colon: ClassVar[re.Pattern[str]]
	_url_encoded_char: ClassVar[re.Pattern[str]]
	_html_entity_like: ClassVar[re.Pattern[str]]
	
	_disallowed_leading_components: ClassVar[tuple[str]]
	_disallowed_trailing_components: ClassVar[tuple[str]]
	_disallowed_components: ClassVar[tuple[str]]
	
	_string: str
	
	def __init__(self, string: str) -> None: ...
	
	@overload
	def __contains__(self, item: str) -> bool: ...
	
	@overload
	def __contains__(self, item: object) -> bool: ...
	
	@overload
	def __eq__(self, other: Self) -> bool: ...
	
	@overload
	def __eq__(self, other: str) -> bool: ...
	
	@overload
	def __eq__(self, other: object) -> bool: ...
	
	def __getitem__(self, item: SupportsIndex | slice) -> str: ...
	
	def __len__(self) -> int:
		'''
		The length of the string, in bytes.
		'''
	
	def __repr__(self) -> str: ...
	
	def __str__(self) -> str: ...
	
	def set(self, new_value: str) -> None:
		'''
		Set a new value for the string.
		'''
	
	def starts_with(self, substring: str) -> bool:
		'''
		Whether the string starts with the given substring.
		'''
	
	def ends_with(self, substring: str) -> bool:
		'''
		Whether the string ends with the given substring.
		'''
	
	def extract(self, start: int, end: Optional[int] = None) -> None:
		'''
		Take a slice of the string from start (inclusive) to end (exclusive)
		and set that as the new string.
		'''
	
	def find_index(self, substring: str) -> int | None:
		'''
		Return the first index at which the substring is found
		or None if there is no such index.
		'''
	
	def remove_unicode_bidirectional_marks(self) -> None:
		'''
		Remove all Unicode bidirectional characters.
		'''
	
	def collapse_whitespaces_series(self) -> None:
		'''
		Collapse every whitespace/underscore sequence into a single space.
		'''
	
	def strip_surrounding_spaces(self) -> None:
		'''
		Remove leading and trailing spaces.
		'''
	
	def sanitize(self) -> None:
		'''
		Shorthand for the following methods:

		* :meth:`remove_unicode_bidirectional_marks`
		* :meth:`collapse_whitespaces_series`
		* :meth:`strip_surrounding_underscore`
		'''
	
	def split_by_first_colon(self) -> tuple[str | None, str]:
		'''
		Split the string by the first colon and any surrounding underscores
		then return a tuple consisting of two string elements.

		If there is no colon, the first element will be None.

		Does not modify the original string.
		'''
	
	def contains_url_encoded_character(self) -> bool:
		'''
		Whether the string has a URL encoded character.
		'''
	
	def contains_html_entity_like(self) -> bool:
		'''
		Whether the string has something looks like an HTML entity
		(i.e. ``&[\dA-Za-z\\u0080-\\uFFFF]+;``).
		'''
	
	def has_relative_path_component(self) -> bool:
		'''
		Whether any of the following is true:
		* self == '.'
		* self == '..'
		* self.starts_with('./')
		* self.starts_with('../')
		* '/./' in self
		* '/../' in self
		* self.ends_with('/.')
		* self.ends_with('/..')
		'''
	
	def _is_relative_path_component(self) -> bool:
		'''
		Whether the string is either '.' or '..'.
		'''
	
	def _starts_with_disallowed_component(self) -> bool:
		'''
		Whether the string starts with a disallowed component.
		'''
	
	def _ends_with_disallowed_component(self) -> bool:
		'''
		Whether the string ends with a disallowed component.
		'''
	
	def _contains_disallowed_component(self) -> bool:
		'''
		Whether the string contains a disallowed component.
		'''
	
	def contains_signature_component(self) -> bool:
		'''
		Whether the string contains triple tildes (``~~~``).
		'''
	
	def remove_fragment_if_any(self) -> None:
		'''
		Remove the fragment, if any.
		'''