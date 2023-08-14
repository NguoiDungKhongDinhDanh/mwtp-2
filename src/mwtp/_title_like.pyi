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

		:param new_value: The new value
		:type new_value: str
		:rtype: None
		'''
	
	def starts_with(self, substring: str) -> bool:
		'''
		Whether the string starts with the given substring.
		
		:param substring: The substring to be checked
		:type substring: str
		:rtype: bool
		'''
	
	def ends_with(self, substring: str) -> bool:
		'''
		Whether the string ends with the given substring.
		
		:param substring: The substring to be checked
		:type substring: str
		:rtype: bool
		'''
	
	def extract(self, start: int, end: Optional[int] = None) -> None:
		'''
		Take a slice of the string from start (inclusive) to end (exclusive)
		and set that as the new string.
		
		:param start: The start index (inclusive)
		:type start: int
		:param end: The end index (exclusive), defaults to None
		:type end: int
		:rtype: None
		'''
	
	def find_index(self, substring: str) -> int | None:
		'''
		Return the first index at which the substring is found
		or None if there is no such index.
		
		:param substring: The substring to search for
		:type substring: str
		:rtype: int | None
		'''
	
	def remove_unicode_bidirectional_marks(self) -> None:
		'''
		Remove all Unicode bidirectional characters.
		
		:rtype: None
		'''
	
	def collapse_whitespaces_series(self) -> None:
		'''
		Collapse every whitespace/underscore sequence into a single space.
		
		:rtype: None
		'''
	
	def strip_surrounding_spaces(self) -> None:
		'''
		Remove leading and trailing spaces.
		
		:rtype: None
		'''
	
	def sanitize(self) -> None:
		'''
		Shorthand for the following methods:

		* :meth:`remove_unicode_bidirectional_marks`
		* :meth:`collapse_whitespaces_series`
		* :meth:`strip_surrounding_underscore`
		
		:rtype: None
		'''
	
	def split_by_first_colon(self) -> tuple[str | None, str]:
		'''
		Split the string by the first colon and any surrounding underscores
		then return a tuple consisting of two string elements.

		If there is no colon, the first element will be None.

		Does not modify the original string.
		
		:rtype: tuple[str | None, str]
		'''
	
	def contains_url_encoded_character(self) -> bool:
		'''
		Whether the string has a URL encoded character.
		
		:rtype: bool
		'''
	
	def contains_html_entity_like(self) -> bool:
		'''
		Whether the string has something looks like an HTML entity
		(i.e. ``&[\dA-Za-z\\u0080-\\uFFFF]+;``).
		
		:rtype: bool
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
		
		:rtype: bool
		'''
	
	def _is_relative_path_component(self) -> bool:
		'''
		Whether the string is either '.' or '..'.
		
		:rtype: bool
		'''
	
	def _starts_with_disallowed_component(self) -> bool:
		'''
		Whether the string starts with a disallowed component.
		
		:rtype: bool
		'''
	
	def _ends_with_disallowed_component(self) -> bool:
		'''
		Whether the string ends with a disallowed component.
		
		:rtype: bool
		'''
	
	def _contains_disallowed_component(self) -> bool:
		'''
		Whether the string contains a disallowed component.
		
		:rtype: bool
		'''
	
	def contains_signature_component(self) -> bool:
		'''
		Whether the string contains triple tildes (``~~~``).
		
		:rtype: bool
		'''
	
	def remove_fragment_if_any(self) -> None:
		'''
		Remove the fragment part, if any.
		
		:rtype: bool
		'''
