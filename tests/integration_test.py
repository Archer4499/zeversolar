import pytest


@pytest.mark.parametrize(argnames=["zeversolar_response", "pac", "energy_today"], argvalues=(
    (
        "1 1 EAB961888888 ABWDWHTQXXXXXXXX M10 16415-562R+16413-561R 15:57 02/02/2023 Error 1 BS15006011999999 V610-01037-04 30 0.0 OK Error",
        30,
        0.0,
    ),
    (
        "1 0 EAB971444444 GHKXWHTQXXXXXXXX M11 19703-826R+17511-707R 15:53 06/03/2022 0 1 EL36806011555555 3187 14.48 OK Error",
        3187,
        14.48,
    ),
    (
        "1 0 EAB971444444 GHKXWHTQXXXXXXXX M11 19703-826R+17511-707R 15:53 06/03/2022 0 1 EL36806011555555 3187 14.20 OK Error",
        3187,
        14.20,
    ),
    (
        "1 1 EAB241666666 ZYXTBGERXXXXXXXX M10 18625-797R+17829-719R 16:22 20/02/2022 1 1 ZS15004513777777 1234 8.9 OK Error",
        1234,
        8.9,
    ),
    (
        "1 1 EAB961777777 WSMQKHTQXXXXXXXX M10 17717-709R+17511-707R 13:59 04/02/2023 0 1 BS20006011888888 226 0.89 OK Error",
        226,
        0.89,
    ),
    (
        "1 1 EAB961555555 KS4GLDHNXXXXXXXX M11 16B21-663R+16B21-658R 16:47 03/02/2023 Error 1 SX0004016666666 2425 19.70 OK Error",
        2425,
        19.70,
    ),

    # Produce a ZeverSolarInvalidData exception since there is no inverter data
    # "1 1 EAB961555555 KS4GLDHNXXXXXXXX M11 16B21-663R+16B21-658R 16:41 03/02/2023 Error 0 Error",

    # Produce a ZeverSolarInvalidData exception
    # "1 0 000000000000 +16B21-658R 15:27 06/02/2023 Error 0 Error",
))
def test_parse_multiple_zeversolar_hardware_version_strings(zeversolar_response: str, pac: int, energy_today: int):
    from zeversolar import ZeverSolarParser
    assert ZeverSolarParser(zeversolar_response).parse().pac == pac
    assert ZeverSolarParser(zeversolar_response).parse().energy_today == energy_today
