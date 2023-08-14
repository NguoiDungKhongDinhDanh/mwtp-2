import re
from typing import (
	ClassVar,
	Literal,
	Mapping,
	NotRequired,
	overload,
	Sequence,
	TypedDict
)

from . import _dcs
from ._alias_record import AliasRecord, NamespaceAlias
from ._namespace_id_map import NamespaceIDMap
from ._title_like import TitleLike
from .title import Title


CasingRule = Literal['first-letter', 'case-sensitive']


class NamespaceDataWithoutAliases(TypedDict):
	id: int
	case: CasingRule
	name: str
	subpages: bool
	content: bool
	nonincludable: bool
	canonical: NotRequired[str]
	namespaceprotection: NotRequired[str]
	defaultcontentmodel: NotRequired[str]


class NamespaceData(NamespaceDataWithoutAliases):
	aliases: set[str]


class Parser:
	'''
	A parser that parse strings using data provided by the user.
	'''
	
	_TITLE_MAX_BYTES: ClassVar[int]
	_ILLEGAL_TITLE_CHARACTER: ClassVar[re.Pattern[str]]
	_TO_UPPER_MAP: ClassVar[dict[int, int]]
	
	_namespace_data: dict[str, _dcs.NamespaceData]
	_namespace_id_map: NamespaceIDMap
	
	def __init__(
		self,
		namespace_data: Mapping[str, NamespaceDataWithoutAliases],
		alias_entries: Sequence[NamespaceAlias]
	) -> None:
		'''
		Construct a new parser object from the given data.
		
		:param namespace_data: A ``Mapping`` from string IDs to namespace data
		:type namespace_data: Mapping[str, NamespaceDataWithoutAliases]
		:param alias_entries: A ``Sequence`` consisting of alias entries
		:type alias_entries: Sequence[NamespaceAlias]
		'''
	
	def _initialize_data_record(
		self,
		namespace_data: Mapping[str, NamespaceDataWithoutAliases],
		alias_record: AliasRecord
	) -> None:
		'''
		Convert all dicts in ``namespace_data`` to
		:class:`_dcs.NamespaceData`.
		
		:param namespace_data: The same data passed to :meth:`__init__`
		:type namespace_data: Mapping[str, NamespaceDataWithoutAliases]
		:param alias_record: \
			An AliasRecord constructed
			using :meth:`__init__`'s alias_entries
		:type alias_record: AliasRecord
		'''
	
	def _initialize_namespace_map(self) -> None:
		'''
		Initialize a namespace-name-(alias)-to-ID map from given data.
		
		:rtype: None
		'''
	
	@property
	def namespace_data(self) -> dict[str, _dcs.NamespaceData]:
		'''
		The data given to and sanitized by the parser.
		
		:rtype: dict[str, _dcs.NamespaceData]
		'''
	
	def parse(self, string: str) -> Title:
		'''
		The main parsing method. Raises :class:`.InvalidTitle`
		if the string is not a valid title.
		
		:param string: The string to parse
		:return: A Title, if parsed successfully
		:rtype: Title
		'''
	
	@overload
	def _apply_casing_rule(
		self,
		page_name: str,
		casing_rule: CasingRule
	) -> str:
		'''
		Apply the casing rule to the given page name.
		
		:param page_name: The page name to be cased
		:type page_name: str
		:param casing_rule: The casing rule
		:type casing_rule: CasingRule
		:return: The page name, cased
		:rtype: str
		'''
	
	@overload
	def _apply_casing_rule(self, page_name: str, casing_rule: str) -> str: ...
	
	def _make_title(self, page_name: str, namespace: int) -> Title:
		'''
		Apply the correct casing rule and construct the title object.
		
		:param page_name: The page name part of the title
		:type page_name: str
		:param namespace: The namespace of the title
		:type namespace: int
		:return: The title object
		:rtype: Title
		'''
	
	def _split_title(self, title_like: TitleLike) -> tuple[int, str]:
		'''
		Split the given title into two parts: namespace and page name.
		
		:param title_like: The TitleLike object to be split
		:type title_like: TitleLike
		:return: A tuple of the namespace and the page name
		:rtype: tuple[int, str]
		'''
	
	def _validate_second_level_namespace(self, page_name: str) -> None:
		'''
		Raise an exception if the given page name
		starts with a valid namespace.
		
		:param page_name: The page name to validate
		:type page_name: str
		:rtype: None
		'''
	
	def _validate_characters(self, page_name: str) -> None:
		'''
		Checks if ``page_name`` contains any illegal characters
		or components. May raise the following exceptions:

		* :class:`exceptions.TitleContainsIllegalCharacters`
		* :class:`exceptions.TitleContainsURLEncodedCharacters`
		* :class:`exceptions.TitleContainsHTMLEntities`
		* :class:`exceptions.TitleHasRelativePathComponents`
		* :class:`exceptions.TitleContainsSignatureComponents`
		
		:param page_name: The page name to validate
		:type page_name: str
		:rtype: None
		'''
	
	def _validate_page_name_length(
		self,
		title_like: TitleLike,
		namespace: int
	) -> None:
		'''
		Raise :class:`exceptions.TitleIsTooLong` if
		the title is not in Special: namespace
		and its length exceeds ``_TITLE_MAX_BYTES``
		
		:param title_like: The TitleLike object to be checked
		:type title_like: TitleLike
		:param namespace: The namespace of the title
		:type namespace: int
		:rtype: bool
		'''
