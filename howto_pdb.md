# PDB file format

A small, highly incomplete, list of what to know about PDB formats (at least, what I found relevant but, concurrently, to so much highlighted).

> WARNING: The PDB format is not updated anymore. Now the standard is the, quite heavy but coherent, mmCIF file format.

## References
- [All entry documentation](https://www.wwpdb.org/documentation/file-format-content/format33/v3.3.html)
- [Coordinates](https://pdb101.rcsb.org/learn/guide-to-understanding-pdb-data/dealing-with-coordinates)
- [Missing residues](https://pdb101.rcsb.org/learn/guide-to-understanding-pdb-data/missing-coordinates-and-biological-assemblies)
- [Correspondence between PDB and mmCIF](https://mmcif.wwpdb.org/docs/pdb_to_pdbx_correspondences.html)


## The list
### General
- If specified a polymer with the characteristic `Protein/Oligosaccharide` (RCSB), then with have an AA bind to another molecule such as a Carbohydrate
- unit cell (x-ray exp) $\neq$ biological unit. [Here the guide from RCSB](https://pdb101.rcsb.org/learn/guide-to-understanding-pdb-data/biological-assemblies)

### Header
- Missing residues are described by the `REMARK 465` record.
- `SEQRES` describe the sequence: it contains missing residues to be compared with `REMARK 465`
- AA that has been modified by the experimentalist, or post-translationally or other, are present with the `HETATM` record and described in the header with the `MODRES`, `HET` and `FORMULA` records
  - Missing atoms that are non-standard AA are not required to be described by a `MODRES` record. Nevertheless, they appear in the `SEQRES` record
- `REMARK 610` describe non-polymer residues with missing atoms
### Coordinates

## Tools (Python)
- `Biopython`
  - [API doc](https://biopython.org/docs/latest/api/) and [general description](https://biopython.org/)
  - very nicely implemented library but the documentation is far from being complete
  - [`PDB`](https://biopython.org/wiki/The_Biopython_Structural_Bioinformatics_FAQ) used to read PDBs, specially `ATOM` records
  - [`SeqIO`](https://biopython.org/wiki/SeqIO) used to read pdb headers and sequences. Used especially for the second case, hence bio-informatics applications.
- `MDAnalysis`
  - Used with MD trajectories for IO and analysis. Complete library with steep learning curve
- [`openmm/pdbfixer`](https://github.com/openmm/pdbfixer)
- [`Modeller`](https://salilab.org/modeller/)
  - VEry complete software for a large range of application, maybe too much, and API doc which is not well structured

