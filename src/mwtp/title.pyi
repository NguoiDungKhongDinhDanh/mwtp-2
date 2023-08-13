import re
from typing import ClassVar, overload, Self

from ._dcs import NamespaceData
from .parser import Parser


# @total_ordering
class Title:
	'''
	Represents a MediaWiki title.

	This class is not meant to be called directly.
	Use :class:`parser.Parser` ``.parse()`` instead.
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
	) -> None: ...
	
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
		'''
	
	@property
	def namespace(self) -> int:
		'''
		The title's namespace ID.
		'''
	
	@property
	def name(self) -> str:
		'''
		The title without the namespace.
		'''
	
	@property
	def namespace_name(self) -> str:
		'''
		The localized name of the title's namespace.
		'''
	
	@property
	def namespace_data(self) -> NamespaceData:
		'''
		An object containing all known information about the title's namespace,
		provided by the parser.
		'''
	
	@property
	def canonical_namespace_name(self) -> str | None:
		'''
		The canonical name of the title's namespace.
		'''
	
	@property
	def associated_namespace(self) -> int | None:
		'''
		The ID of the talk or subject namespace to which the title's
		namespace is associated with.
		'''
	
	@property
	def associated_namespace_name(self) -> str | None:
		'''
		The localized name of the title's associated namespace.
		'''
	
	@property
	def associated_namespace_data(self) -> NamespaceData | None:
		'''
		An object containing all known information about the title's associated
		namespace, provided by the parser.
		'''
	
	@property
	def in_content_namespace(self) -> bool:
		'''
		Whether the namespace of the title is a content namespace.
		'''
	
	@property
	def title_fragments(self) -> tuple[str]:
		'''
		If the namespace has ``.subpages == True``,
		returns a tuple of strings generated from
		splitting the title by '/'.

		Else, returns the name wrapped in a tuple.
		'''
	
	@property
	def root(self) -> Self:
		'''
		A Title object representing the root title
		of this title.
		'''
	
	@property
	def base(self) -> Self:
		'''
		A Title object representing the parent title
		of this title.
		'''
	
	@property
	def tail(self) -> str:
		'''
		The rightmost fragment of the title.
		'''
	
	@property
	def is_subpage(self) -> bool:
		'''
		Whether the title has a parent title.
		'''
	
	@property
	def extension(self) -> str | None:
		'''
		The extension part of a file name, if any.
		'''
	
	@property
	def associated(self) -> Self | None:
		'''
		The title associated to this title.
		'''
	
	@property
	def subject(self) -> Self:
		'''
		The subject title correspond to this title.
		'''
	
	@property
	def talk(self) -> Self | None:
		'''
		The talk title correspond to this title.
		'''
