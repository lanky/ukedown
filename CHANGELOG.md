# Changelog#

## v2.2.1 - BUGFIX release

- fixes issues with tests and GH Actions

b7c1d34 - (HEAD -> master, origin/master, origin/HEAD) Update dependencies and lockfile (2 hours ago) <Stuart Sears>
eea9d85 - Update Vox test patterns (2 hours ago) <Stuart Sears>
cad2486 - Updated Github Actions (2 hours ago) <Stuart Sears>
275d7a0 - Bump to v2.2.0, add URLS and changelogs to package (2 hours ago) <Stuart Sears>
2fbd2d1 - Remove unused TagProcessor (2 hours ago) <Stuart Sears>
2220219 - Update python-package.yml (2 hours ago) <Stuart Sears>
8873393 - linting (2 hours ago) <Stuart Sears>


## v2.2.0
c7a47c6 - (HEAD -> postprocessing_vox) Remove unused TagProcessor
95f9f08 - (origin/postprocessing_vox) linting
9a1280b - Fix parameter typo in HeaderProcessor
afaea8d - Tidy up parametersin UkeBookExtension
6314279 - Add VoxPostProcessor for future use
1df948d - Move to InlineProcessor from inlinePattern
dbac90b - Make backing vox pattern much simpler
fc0df36 - ruff linting
c1b3783 - Import tidying
1ca972d - Add grouping to chord pattern


## v2.1.1
777bb12 BUGFIX: silly typo in repeats pattern   (HEAD -> refs/heads/master)

## v.2.1.0
95dce5e  (HEAD -> refs/heads/master, tag: refs/tags/v2.1.0)
d9ad3a6 permit additional punctuation chars in vox
8fb2df0 reflowed for linelengths (linting)
b47885c Use poetry in CI
8397967 Re-enable CI tests with pytest
25992d2 Add some simple unit tests of regex patterns
df27c9d Add pytest as a dev dependency
702dee3 updates to README with more examples   (refs/heads/pytest)
ac33f58 Adds example CSS file  lanky@behemoth:ukedown (master *$%>)

## v 2.0.0
44e9aa0 (HEAD -> master, tag: v2.0.0) Add poetry lockfile
75cb4dd (origin/master, origin/HEAD) python project config using poetry
597e39f reformatted with black
8c8688b (markdown3) Merge pull request #1 from lanky/markdown3
989f9c9 (origin/markdown3) disables pytest until we actually have tests. If ever.
3e810cb Add package builder action
48cf0cc disables pytest until we actually have tests. If ever.
11a4e17 much blackness, plus extension register updates
61c71ec Add package builder action

## v1.0.0 - First PyPi release
efc9102 (tag: v1.0.0) new major version, with versioned deps
e9e7252 README updates, URL correction etc
d24ee73 update to Markdown 3 API, parametrise processors
c67a1bc fixes ElementTree warnings
92d6120 ignore backup files and build artifacts
a167d22 Corrects pypi username
e8a298c corrects type in long_desceription assignment
36debf8 added dependencies to setup.py
386413e Adds license and license headers for GPL v3+
b2198ca move package contents into ukedown subdir
bcae6c2 permits single quotes in backing vox
0495226 removes support for perf notes in chord pattern
11b99ef renders [section] as span, not h2
e544ecf updates chord recognition patterns
7d9c2f5 made notes regex more generic (anything in {})
f45c0cc reverted multiline parsing to fix box detection
4f45f5f Permit '/' in performance notes
9f51836 ukedown updated to stop box sections collapsing together
b0958cd enabled 'notes' markup in udn ({NOTE}) for performance notes
17c66e5 Added support for X/Y to chord patterns ('/')
385caa3 updated translation table to include ellipsis
7718fd6 Migrate to  python3 using 2to3
eb49a5f Multiple updates to udn core
7ef4f2d split out regex and translation tables
e477ffe renamed CollapseDivProcessor to CollapseChildProcessor
e9e3daf header patterns now work inside box sections
d92c0c9 added inline patterns for vox and notes
8f5bb6a added NOTES and VOX patterns
964cb57 treeprocessor for paragraph merging
d15ac69 refactored ukedown extension into ukedown/udn.py Updated mdsession to use this

