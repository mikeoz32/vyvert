from typing import Annotated
import pytest
from vyvert.datastructures import Depends

from vyvert.utils import call_with_deps

class Dependency:
    def __init__(self, sub_dependency: str) -> None:
        self.data = sub_dependency

async def function(dep: Annotated[Dependency, Depends()]):
    return dep

@pytest.mark.asyncio
async def test_resolve_class():
    result = await call_with_deps(function, ctx={"sub_dependency":"test"})
    assert result is not None
    assert result.data == "test"
