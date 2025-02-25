===================================================================
antsibull-docs -- Ansible Documentation Build Scripts Release Notes
===================================================================

.. contents:: Topics


v2.0.0
======

Release Summary
---------------

Major new release that drops support for older Python and Ansible/ansible-base/ansible-core versions.

Major Changes
-------------

- Change pyproject build backend from ``poetry-core`` to ``hatchling``. ``pip install antsibull-docs`` works exactly the same as before, but some users may be affected depending on how they build/install the project (https://github.com/ansible-community/antsibull-docs/pull/115).

Minor Changes
-------------

- Allow to use the currently installed ansible-core version for the ``devel`` and ``stable`` subcommands (https://github.com/ansible-community/antsibull-docs/pull/121).
- Ansibull-docs now no longer depends directly on ``sh`` (https://github.com/ansible-community/antsibull-docs/pull/122).
- Bump version range of antsibull-docs requirement written by ``sphinx-init`` subcommand to ``>= 2.0.0, < 3.0.0``. Previously, this was set to ``>=2.0.0a2, <3.0.0`` (https://github.com/ansible-community/antsibull-docs/pull/151).
- Now depends antsibull-core 2.0.0 or newer; antsibull-core 1.x.y is no longer supported (https://github.com/ansible-community/antsibull-docs/pull/122).
- Remove residual compatability code for Python 3.6 and 3.7 (https://github.com/ansible-community/antsibull-docs/pulls/70).
- Support a per-collection docs config file ``docs/docsite/config.yml``. It is also linted by the ``lint-collection-docs`` subcommand (https://github.com/ansible-community/antsibull-docs/pull/134).
- The antsibull-docs requirement in the ``requirements.txt`` file created by the sphinx-init subcommand now has version range ``>= 2.0.0, < 3.0.0`` (https://github.com/ansible-community/antsibull-docs/pull/126).
- The dependency `antsibull-docs-parser <https://github.com/ansible-community/antsibull-docs-parser>`__ has been added and is used for processing Ansible markup (https://github.com/ansible-community/antsibull-docs/pull/124).

Breaking Changes / Porting Guide
--------------------------------

- Disable flatmapping for all collections except community.general < 6.0.0 and community.network < 5.0.0. You can enable flatmapping for your collection by setting ``flatmap: true`` in ``docs/docsite/config.yml`` (https://github.com/ansible-community/antsibull-docs/pull/134).
- Drop support for Python 3.6, 3.7, and 3.8 (https://github.com/ansible-community/antsibull-docs/pull/115)."
- No longer removes ``PYTHONPATH`` from the environment when calling ``ansible``, ``ansible-galaxy``, or ``ansible-doc`` outside a self-created venv (https://github.com/ansible-community/antsibull-docs/pull/121).
- No longer supports Ansible 2.9, ansible-base 2.10, and ansible-core 2.11 and 2.12. The minimum required ansible-core version is 2.13. This allows for simpler and more efficient docs parsing and information retrieval (https://github.com/ansible-community/antsibull-docs/pull/120).
- The ``ansible-doc`` and ``ansible-internal`` values for ``doc_parsing_backend`` in the configuration file have been removed. Change the value to ``auto`` for best compatibility (https://github.com/ansible-community/antsibull-docs/pull/120).

Bugfixes
--------

- Bump version range of antsibull-docs requirement written by ``sphinx-init`` subcommand to ``>= 2.0.0a2, < 3.0.0``. Previously, this was set to ``>=2.0.0, <3.0.0`` which could not be satisfied (https://github.com/ansible-community/antsibull-docs/pull/149).
- Use ``doc_parsing_backend`` from the application context instead of the library context. This prevents removal of ``doc_parsing_backend`` from the antsibull-core library context (https://github.com/ansible-community/antsibull-docs/pull/125).

v1.11.0
=======

Release Summary
---------------

Feature release.

Minor Changes
-------------

- Add support for semantic markup in roles (https://github.com/ansible-community/antsibull-docs/pull/113).
- Internal refactoring of markup code (https://github.com/ansible-community/antsibull-docs/pull/108).
- The ``lint-collection-docs`` subcommand can be told not to run rstcheck when ``--plugin-docs`` is used by passing ``--skip-rstcheck``. This speeds up testing for large collections (https://github.com/ansible-community/antsibull-docs/pull/112).
- The ``lint-collection-docs`` subcommand will now also validate Ansible markup when ``--plugin-docs`` is passed. It can also ensure that no semantic markup is used with the new ``--disallow-semantic-markup`` option. This can for example be used by collections to avoid semantic markup being backported to older stable branches (https://github.com/ansible-community/antsibull-docs/pull/112).

v1.10.0
=======

Release Summary
---------------

Bugfix and feature release.

Major Changes
-------------

- Support new semantic markup in documentation (https://github.com/ansible-community/antsibull-docs/pull/4).

Minor Changes
-------------

- Add a note about the ordering of positional and named parameter to the plugin page. Also mention positional and keyword parameters for lookups (https://github.com/ansible-community/antsibull-docs/pull/101).
- Update schema for roles argument spec to allow specifying attributes on the entrypoint level. These are now also rendered when present (https://github.com/ansible-community/antsibull-docs/pull/103).

Bugfixes
--------

- Explicitly declare the ``sh`` dependency and limit it to before 2.0.0. Also explicitly declare the dependencies on ``pydantic``, ``semantic_version``, ``aiohttp``, ``twiggy``, and ``PyYAML`` (https://github.com/ansible-community/antsibull-docs/pull/99).
- Restrict the ``pydantic`` dependency to major version 1 (https://github.com/ansible-community/antsibull-docs/pull/102).

v1.9.0
======

Release Summary
---------------

Feature release.

Minor Changes
-------------

- Improve build script generated by ``antsibull-docs sphinx-init`` to change to the directory where the script is located, instead of hardcoding the script's path. This also fixed the existing bug that the path was not quoted (https://github.com/ansible-community/antsibull-docs/issues/91, https://github.com/ansible-community/antsibull-docs/pull/92).
- Show callback plugin type on callback plugin pages. Also write callback indexes by callback plugin type (https://github.com/ansible-community/antsibull-docs/issues/89, https://github.com/ansible-community/antsibull-docs/pull/90).

v1.8.2
======

Release Summary
---------------

Bugfix release.

Bugfixes
--------

- Fix the new options ``--extra-html-context`` and ``--extra-html-theme-options`` of the ``sphinx-init`` subcommand (https://github.com/ansible-community/antsibull-docs/pull/86).

v1.8.1
======

Release Summary
---------------

Bugfix release.

Bugfixes
--------

- When creating toctrees for breadcrumbs, place subtree for a plugin type in the plugin type's section (https://github.com/ansible-community/antsibull-docs/pull/83).

v1.8.0
======

Release Summary
---------------

Feature and bugfix release.

Minor Changes
-------------

- Add new options ``--project``, ``--copyright``, ``--title``, ``--html-short-title``, ``--extra-conf``, ``--extra-html-context``, and ``--extra-html-theme-options`` to the ``sphinx-init`` subcommand to allow to customize the generated ``conf.py`` Sphinx configuration (https://github.com/ansible-community/antsibull-docs/pull/77).
- Automatically use a module's or plugin's short description as the "See also" description if no description is provided (https://github.com/ansible-community/antsibull-docs/issues/64, https://github.com/ansible-community/antsibull-docs/pull/74).
- It is now possible to provide a path to an existing file to be used as ``rst/index.rst`` for ``antsibull-docs sphinx-init`` (https://github.com/ansible-community/antsibull-docs/pull/68).
- Make compatible with antsibull-core 2.x.y (https://github.com/ansible-community/antsibull-docs/pull/78).
- Remove support for ``forced_action_plugin``, a module attribute that was removed during the development phase of attributes (https://github.com/ansible-community/antsibull-docs/pull/63).
- Stop mentioning the version features were added for Ansible if the Ansible version is before 2.7 (https://github.com/ansible-community/antsibull-docs/pull/76).
- The default ``index.rst`` created by ``antsibull-docs sphinx-init`` includes the new environment variable index (https://github.com/ansible-community/antsibull-docs/pull/80).
- Use correct markup (``envvar`` role) for environment variables. Compile an index of all environment variables used by plugins (https://github.com/ansible-community/antsibull-docs/pull/73).

Bugfixes
--------

- Make sure that ``build.sh`` created by the ``sphinx-init`` subcommand sets proper permissions for antsibull-docs on the ``temp-rst`` directory it creates (https://github.com/ansible-community/antsibull-docs/pull/79).

v1.7.4
======

Release Summary
---------------

Bugfix release.

Bugfixes
--------

- Removed ``sphinx`` restriction in ``requirements.txt`` file created by ``antsibull-docs sphinx-init`` since the bug in ``sphinx-rtd-theme`` has been fixed (https://github.com/ansible-community/antsibull-docs/pull/69).
- The license header for the template for the ``rst/index.rst`` file created by ``antsibull-docs sphinx-init`` was commented incorrectly and thus showed up in the templated file (https://github.com/ansible-community/antsibull-docs/pull/67).
- When using ``--squash-hierarchy``, do not mention the list of collections on the collection's index page (https://github.com/ansible-community/antsibull-docs/pull/72).

v1.7.3
======

Release Summary
---------------

Bugfix release.

Bugfixes
--------

- Fix rendering of the ``action_group`` attribute (https://github.com/ansible-community/antsibull-docs/pull/62).

v1.7.2
======

Release Summary
---------------

Bugfix release.

Bugfixes
--------

- Fix ``version_added`` processing for ansible.builtin 0.x to represent this as ``Ansible 0.x`` instead of ``ansible-core 0.x`` (https://github.com/ansible-community/antsibull-docs/pull/61).

v1.7.1
======

Release Summary
---------------

Bugfix release.

Bugfixes
--------

- Prevent crash during ``stable`` docsite build when ``_python`` entry is present in deps file (https://github.com/ansible-community/antsibull-docs/pull/57).

v1.7.0
======

Release Summary
---------------

Bugfix and feature release.

Minor Changes
-------------

- Add ``--intersphinx`` option to the ``sphinx-init`` subcommand to allow adding additional ``intersphinx_mapping`` entries to ``conf.py`` (https://github.com/ansible-community/antsibull-docs/issues/35, https://github.com/ansible-community/antsibull-docs/pull/44).
- Allow the ``toctree`` entries for in a collection's ``docs/docsite/extra-docs.yml`` to be a dictionary with ``ref`` and ``title`` keys instead of just a reference as a string (https://github.com/ansible-community/antsibull-docs/pull/45).
- Antsibull-docs now depends on `packaging <https://pypi.org/project/packaging/>`__ (https://github.com/ansible-community/antsibull-docs/pull/49).
- The collection index pages now contain the supported versions of ansible-core of the collection in case collection's ``meta/runtime.yml`` specifies ``requires_ansible`` (https://github.com/ansible-community/antsibull-docs/issues/48, https://github.com/ansible-community/antsibull-docs/pull/49).
- The output of the ``lint-collection-docs`` command has been improved; in particular multi-line messages are now indented (https://github.com/ansible-community/antsibull-docs/pull/52).
- Use ``ansible --version`` to figure out ansible-core version when ansible-core is not installed for the same Python interpreter / venv that is used for antsibull-docs (https://github.com/ansible-community/antsibull-docs/pull/50).
- Use code formatting for all values, such as choice entries, defaults, and samples (https://github.com/ansible-community/antsibull-docs/issues/38, https://github.com/ansible-community/antsibull-docs/pull/42).

Bugfixes
--------

- Avoid long aliases list to make left column too wide (https://github.com/ansible-collections/amazon.aws/issues/1101, https://github.com/ansible-community/antsibull-docs/pull/54).
- Make ``lint-collection-docs --plugin-docs`` subcommand actually work (https://github.com/ansible-community/antsibull-docs/pull/47).

v1.6.1
======

Release Summary
---------------

Bugfix release for ansible-core 2.14.

Bugfixes
--------

- Fix formulation of top-level ``version_added`` (https://github.com/ansible-community/antsibull-docs/pull/43).

v1.6.0
======

Release Summary
---------------

Bugfix and feature release.

Minor Changes
-------------

- Allow to specify choices as dictionary instead of list (https://github.com/ansible-community/antsibull-docs/pull/36).
- Use JSON serializer to format choices (https://github.com/ansible-community/antsibull-docs/pull/37).
- Use special serializer to format INI values in examples (https://github.com/ansible-community/antsibull-docs/pull/37).

Bugfixes
--------

- Avoid collection names with ``_`` in them appear wrongly escaped in the HTML output (https://github.com/ansible-community/antsibull-docs/pull/41).
- For INI examples which have no default, write ``VALUE`` as intended instead of ``None`` (https://github.com/ansible-community/antsibull-docs/pull/37).
- Format lists correctly for INI examples (https://github.com/ansible-community/antsibull-docs/pull/37).
- The ``sphinx-init`` subcommand's ``requirement.txt`` file avoids Sphinx 5.2.0.post0, which triggers a bug in sphinx-rtd-theme which happens to be the parent theme of the default theme sphinx_ansible_theme used by ``sphinx-init`` (https://github.com/ansible-community/antsibull-docs/issues/39, https://github.com/ansible-community/antsibull-docs/pull/40).

v1.5.0
======

Release Summary
---------------

Feature and bugfix release.

Minor Changes
-------------

- Detect filter and test plugin aliases and avoid them being emitted multiple times. Instead insert redirects so that stub pages will be created (https://github.com/ansible-community/antsibull-docs/pull/33).
- Replace ``ansible.builtin`` with ``ansible-core``, ``ansible-base``, or ``Ansible`` in version added collection names. Also write ``<collection_name> <version>`` instead of ``<version> of <collection_name>`` (https://github.com/ansible-community/antsibull-docs/pull/34).

Bugfixes
--------

- Fix escaping of collection names in version added statements, and fix collection names for roles options (https://github.com/ansible-community/antsibull-docs/pull/34).

v1.4.0
======

Release Summary
---------------

Feature and bugfix release.

Minor Changes
-------------

- The ``sphinx-init`` subcommand now also creates an ``antsibull-docs.cfg`` file and moves configuration settings from CLI flags in ``build.sh`` to this configuration file (https://github.com/ansible-community/antsibull-docs/pull/26).
- There are two new options for explicitly specified configuration files named ``collection_url`` and ``collection_install``. These allow to override the URLs pointing to collections (default link to galaxy.ansible.com), and the commands to install collections (use ``ansible-galaxy collection install`` by default). This can be useful when documenting (internal) collections that are not available on Ansible Galaxy. The default ``antsibull-docs.cfg`` generated by the ``sphinx-init`` subcommand shows how this can be configured (https://github.com/ansible-community/antsibull-docs/issues/15, https://github.com/ansible-community/antsibull-docs/pull/26).
- When generating plugin error pages, or showing non-fatal errors in plugins or roles, link to the collection's issue tracker instead of the collection's URL if available (https://github.com/ansible-community/antsibull-docs/pull/29).

Bugfixes
--------

- Make handling of bad documentation more robust when certain values are ``None`` while the keys are present (https://github.com/ansible-community/antsibull-docs/pull/32).

v1.3.0
======

Release Summary
---------------

Feature and bugfix release.

Minor Changes
-------------

- Ensure that values for ``default``, ``choices``, and ``sample`` use the types specified for the option / return value (https://github.com/ansible-community/antsibull-docs/pull/19).
- If a plugin or module has requirements listed, add a disclaimer next to the installation line at the top that further requirements are needed (https://github.com/ansible-community/antsibull-docs/issues/23, https://github.com/ansible-community/antsibull-docs/pull/24).
- Show the 'you might already have this collection installed if you are using the ``ansible`` package' disclaimer for plugins only for official docsite builds (subcommands ``devel`` and ``stable``). Also include this disclaimer for roles on official docsite builds (https://github.com/ansible-community/antsibull-docs/pull/25).
- Use ``true`` and ``false`` for booleans instead of ``yes`` and ``no`` (https://github.com/ansible-community/community-topics/issues/116, https://github.com/ansible-community/antsibull-docs/pull/19).
- When processing formatting directives, make sure to properly escape all other text for RST respectively HTML instead of including it verbatim (https://github.com/ansible-community/antsibull-docs/issues/21, https://github.com/ansible-community/antsibull-docs/pull/22).

Bugfixes
--------

- Improve indentation of HTML blocks for tables to avoid edge cases which generate invalid RST (https://github.com/ansible-community/antsibull-docs/pull/22).

v1.2.2
======

Release Summary
---------------

Bugfix release.

Bugfixes
--------

- Fix rstcheck-core support (https://github.com/ansible-community/antsibull-docs/pull/20).

v1.2.1
======

Release Summary
---------------

Bugfix release.

Bugfixes
--------

- Do not escape ``<``, ``>``, ``&``, and ``'`` in JSONified defaults and examples as the `Jinja2 tojson filter <https://jinja.palletsprojects.com/en/2.11.x/templates/#tojson>`_ does. Also improve formatting by making sure ``,`` is followed by a space (https://github.com/ansible-community/antsibull-docs/pull/18).
- The collection filter was ignored when parsing the ``ansible-galaxy collection list`` output for the docs build (https://github.com/ansible-community/antsibull-docs/issues/16, https://github.com/ansible-community/antsibull-docs/pull/17).

v1.2.0
======

Release Summary
---------------

Feature and bugfix release.

Minor Changes
-------------

- Support plugin ``seealso`` from the `semantic markup specification <https://hackmd.io/VjN60QSoRSSeRfvGmOH1lQ?both>`__ (https://github.com/ansible-community/antsibull-docs/pull/8).
- The ``lint-collection-docs`` subcommand has a new boolean flag ``--plugin-docs`` which renders the plugin docs to RST and validates them with rstcheck. This can be used as a lighter version of rendering the docsite in CI (https://github.com/ansible-community/antsibull-docs/pull/12).
- The files in the source repository now follow the `REUSE Specification <https://reuse.software/spec/>`_. The only exceptions are changelog fragments in ``changelogs/fragments/`` (https://github.com/ansible-community/antsibull-docs/pull/14).

Bugfixes
--------

- Make sure that ``_input`` does not show up twice for test or filter arguments when the plugin mentions it in ``positional`` (https://github.com/ansible-community/antsibull-docs/pull/10).
- Mark rstcheck 4.x and 5.x as compatible. Support rstcheck 6.x as well (https://github.com/ansible-community/antsibull-docs/pull/13).

v1.1.0
======

Release Summary
---------------

Feature release with support for ansible-core 2.14's sidecar docs feature.

Minor Changes
-------------

- If lookup plugins have a single return value starting with ``_``, that return value is now labelled ``Return value`` (https://github.com/ansible-community/antsibull-docs/pull/6).
- If lookup plugins have an option called ``_terms``, it is now shown in its own section ``Terms``, and not in the regular ``Parameters`` section (https://github.com/ansible-community/antsibull-docs/pull/6).
- More robust handling of parsing errors when ansible-doc was unable to extract documentation (https://github.com/ansible-community/antsibull-docs/pull/6).
- Support parameter type ``any``, and show ``raw`` as ``any`` (https://github.com/ansible-community/antsibull-docs/pull/6).
- Support test and filter plugins when ansible-core 2.14+ is used. This works with the current ``devel`` branch of ansible-core (https://github.com/ansible-community/antsibull-docs/pull/6).

v1.0.1
======

Release Summary
---------------

Bugfix release.

Bugfixes
--------

- Make sure that aliases of module/plugin options and return values that result in identical RST labels under docutil's normalization are only emitted once (https://github.com/ansible-community/antsibull-docs/pull/7).
- Properly escape module/plugin option and return value slugs in generated HTML (https://github.com/ansible-community/antsibull-docs/pull/7).

v1.0.0
======

Release Summary
---------------

First stable release.

Major Changes
-------------

- From version 1.0.0 on, antsibull-docs is sticking to semantic versioning and aims at providing no backwards compatibility breaking changes **to the command line API (antsibull-docs)** during a major release cycle. We explicitly exclude code compatibility. **antsibull-docs is not supposed to be used as a library,** and when used as a library it might not conform to semantic versioning (https://github.com/ansible-community/antsibull-docs/pull/2).

Minor Changes
-------------

- Only mention 'These are the collections with docs hosted on docs.ansible.com' for ``stable`` and ``devel`` subcommands (https://github.com/ansible-community/antsibull-docs/pull/3).
- Stop using some API from antsibull-core that is being removed (https://github.com/ansible-community/antsibull-docs/pull/1).

v0.1.0
======

Release Summary
---------------

Initial release. The ``antsibull-docs`` tool is compatible to the one from antsibull 0.43.0.
