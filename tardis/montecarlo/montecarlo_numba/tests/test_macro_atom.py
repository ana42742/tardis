import pytest
import tardis.montecarlo.montecarlo_numba.macro_atom as macro_atom
import numpy as np


@pytest.mark.parametrize(
    ["seed", "expected"],
    [(1963, 10015), (1, 9993), (2111963, 17296), (10000, 9993)],
)
def test_macro_atom(
    static_packet,
    verysimple_numba_plasma,
    verysimple_numba_model,
    set_seed_fixture,
    seed,
    expected,
):
    set_seed_fixture(seed)
    static_packet.initialize_line_id(
        verysimple_numba_plasma, verysimple_numba_model
    )
    activation_level_id = verysimple_numba_plasma.line2macro_level_upper[
        static_packet.next_line_id
    ]
    result, transition_type = macro_atom.macro_atom(
        activation_level_id,
        static_packet.current_shell_id,
        verysimple_numba_plasma,
    )
    assert result == expected
    assert transition_type == -1  # line transition
