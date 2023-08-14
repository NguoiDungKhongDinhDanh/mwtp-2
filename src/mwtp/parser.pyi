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
	Construct a parser from given namespace data.
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
	) -> None: ...
	
	def _initialize_data_record(
		self,
		namespace_data: Mapping[str, NamespaceDataWithoutAliases],
		alias_record: AliasRecord
	) -> None:
		'''
		Convert all dicts in ``namespace_data`` to
		:class:`_dcs.NamespaceData`.
		'''
	
	def _initialize_namespace_map(self) -> None:
		'''
		Initialize a namespace-name-(alias)-to-ID map from given data.
		'''
	
	@property
	def namespace_data(self) -> dict[str, _dcs.NamespaceData]:
		'''
		The data given to and sanitized by the parser.
		'''
	
	def parse(self, string: str) -> Title:
		'''
		The main parsing method.
		'''
	
	@overload
	def _apply_casing_rule(
		self,
		page_name: str,
		casing_rule: CasingRule
	) -> str:
		'''
		Apply the casing rule to the given page name.
		'''
	
	@overload
	def _apply_casing_rule(self, page_name: str, casing_rule: str) -> str: ...
	
	def _make_title(self, page_name: str, namespace: int) -> Title:
		'''
		Responsible for applying the correct casing rule before
		creating the title object.
		'''
	
	def _split_title(self, title_like: TitleLike) -> tuple[int, str]:
		'''
		Split the given title into two parts: namespace and page name.
		'''
	
	def _validate_second_level_namespace(self, page_name: str) -> None:
		'''
		Raise an exception if the given page name
		starts with a valid namespace.
		'''
	
	def _validate_characters(self, page_name: str) -> None:
		'''
		May raise the following exceptions:

		* :class:`exceptions.TitleContainsIllegalCharacters`
		* :class:`exceptions.TitleContainsURLEncodedCharacters`
		* :class:`exceptions.TitleContainsHTMLEntities`
		* :class:`exceptions.TitleHasRelativePathComponents`
		* :class:`exceptions.TitleContainsSignatureComponents`
		'''
	
	def _validate_page_name_length(
		self,
		page_name: TitleLike,
		namespace: int
	) -> None:
		'''
		Raise :class:`exceptions.TitleIsTooLong` if
		title is in File: namespace and its length
		exceeds ``_FILENAME_MAX_BYTES``
		'''
