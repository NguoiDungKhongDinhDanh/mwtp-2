from typing import Sequence, TypedDict


class NamespaceAlias(TypedDict):
	id: int
	alias: str


class AliasRecord:
	'''
	A record that maps namespace identifiers to their corresponding aliases.
	'''
	
	_record: dict[int, set[str]]
	
	def __init__(self, data: Sequence[NamespaceAlias]) -> None: ...
	
	def __getitem__(self, item: int | str) -> set[str]: ...
	
	def __repr__(self) -> str: ...