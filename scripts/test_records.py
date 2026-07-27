from scripts.chunker import Chunk
from scripts.records import build_records, chunk_id, page_url_from_src

SITE = "https://docs.chiligrafx.com/"


def test_index_md_maps_to_trailing_slash():
    assert page_url_from_src("CHILI-GraFx/admin/index.md", SITE) == \
        "https://docs.chiligrafx.com/CHILI-GraFx/admin/"


def test_root_index_maps_to_site_root():
    assert page_url_from_src("index.md", SITE) == "https://docs.chiligrafx.com/"


def test_plain_md_maps_to_trailing_slash():
    assert page_url_from_src("GraFx-Studio/overview.md", SITE) == \
        "https://docs.chiligrafx.com/GraFx-Studio/overview/"


def test_chunk_id_is_stable_and_position_sensitive():
    a = chunk_id("x/index.md", "Intro", 0)
    assert a == chunk_id("x/index.md", "Intro", 0)   # stable across runs
    assert a != chunk_id("x/index.md", "Intro", 1)   # position matters
    assert a != chunk_id("y/index.md", "Intro", 0)   # path matters


def test_build_records_zips_and_carries_model_dim():
    chunks = [Chunk("Intro", "alpha"), Chunk("Intro", "beta")]
    embs = [[0.1, 0.2], [0.3, 0.4]]
    recs = build_records("p/index.md", SITE, chunks, embs, model="text-embedding-3-small", dim=2)
    assert [r.chunk_text for r in recs] == ["alpha", "beta"]
    assert all(r.model == "text-embedding-3-small" and r.dim == 2 for r in recs)
    assert recs[0].page_url == "https://docs.chiligrafx.com/p/"
    assert recs[0].id != recs[1].id


def test_build_records_rejects_length_mismatch():
    import pytest
    with pytest.raises(ValueError):
        build_records("p/index.md", SITE, [Chunk("s", "t")], [], model="m", dim=2)
