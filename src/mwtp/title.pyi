import re
from functools import total_ordering
from typing import ClassVar, overload, Self

from ._dcs import NamespaceData
from .parser import Parser


@total_ordering
class Title:
	'''
	Represents a MediaWiki title.

	This class is not meant to be used directly.
	Use :meth:`parser.Parser.parse()` instead.
	'''
	
	_extension: ClassVar[re.Pattern[str]]
	
	_parser: Parser
	_name: str
	_namespace: int
	
	def __init__(
		self,
		name: str, *,
		namespace: int,
		parser: Parser
	) -> None:
		'''
		Construct a Title object.
		
		:param name: The page name part of the title
		:type name: str
		:param namespace: The namespace of the title
		:type namespace: int
		:param parser: The parser which constructed the title
		:type parser: Parser
		'''
	
	def __str__(self) -> str: ...
	
	def __repr__(self) -> str: ...
	
	def __hash__(self) -> int: ...
	
	@overload
	def __lt__(self, other: Self) -> bool: ...
	
	@overload
	def __lt__(self, other: str) -> bool: ...
	
	@overload
	def __eq__(self, other: Self) -> bool: ...
	
	@overload
	def __eq__(self, other: str) -> bool: ...
	
	@overload
	def __eq__(self, other: object) -> bool: ...
	
	def __truediv__(self, other: str) -> Self: ...
	
	@property
	def full_name(self) -> str:
		'''
		The full title (i.e. `Namespace:Title` or `Title`).
		
		:rtype: str
		'''
	
	@property
	def namespace(self) -> int:
		'''
		The title's namespace ID.
		
		:rtype: int
		'''
	
	@property
	def name(self) -> str:
		'''
		The title without the namespace.
		
		:rtype: str
		'''
	
	@property
	def namespace_name(self) -> str:
		'''
		The localized name of the title's namespace.
		
		:rtype: str
		'''
	
	@property
	def namespace_data(self) -> NamespaceData:
		'''
		An object containing all known information
		about the title's namespace.
		This is retrieved from the parser.
		
		:rtype: NamespaceData
		'''
	
	@property
	def canonical_namespace_name(self) -> str | None:
		'''
		The canonical name of the title's namespace.
		
		:rtype: str | None
		'''
	
	@property
	def associated_namespace(self) -> int | None:
		'''
		The ID of the talk or subject namespace to which
		the title's namespace is associated with.
		
		:rtype: int | None
		'''
	
	@property
	def associated_namespace_name(self) -> str | None:
		'''
		The localized name of the title's associated namespace.
		
		:rtype: str | None
		'''
	
	@property
	def associated_namespace_data(self) -> NamespaceData | None:
		'''
		An object containing all known information about
		the title's associated namespace or None if there
		is no such namespace.
		This is retrieved from the parser.
		
		:rtype: NamespaceData | None
		'''
	
	@property
	def in_content_namespace(self) -> bool:
		'''
		Whether the namespace of the title is a content namespace.
		
		:rtype: bool
		'''
	
	@property
	def title_fragments(self) -> tuple[str]:
		'''
		If the namespace has ``.subpages == True``,
		returns a tuple of strings generated from
		splitting the title by '/'.

		Else, returns the name wrapped in a tuple.
		
		:rtype: tuple[str]
		'''
	
	@property
	def root(self) -> Self:
		'''
		A Title object representing the root title
		of this title.
		
		:rtype: Self
		'''
	
	@property
	def base(self) -> Self:
		'''
		A Title object representing the parent title
		of this title.
		
		:rtype: Self
		'''
	
	@property
	def tail(self) -> str:
		'''
		The rightmost fragment of the title.
		
		:rtype: str
		'''
	
	@property
	def is_subpage(self) -> bool:
		'''
		Whether the title has a parent title.
		
		:rtype: bool
		'''
	
	@property
	def extension(self) -> str | None:
		'''
		The extension part of a file name, if any.
		
		:rtype: str | None
		'''
	
	@property
	def associated(self) -> Self | None:
		'''
		The title associated to this title, or None
		if there is no such title.
		
		:rtype: Self | None
		'''
	
	@property
	def subject(self) -> Self:
		'''
		The subject title correspond to this title.
		Can be itself if it is a subject title.
		
		:rtype: Self
		'''
	
	@property
	def talk(self) -> Self | None:
		'''
		The talk title correspond to this title,
		or None if there is no such title.
		
		:rtype: Self | None
		'''
