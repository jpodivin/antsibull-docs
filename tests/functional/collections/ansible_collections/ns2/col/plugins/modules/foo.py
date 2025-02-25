#!/usr/bin/python
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Ansible Project

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = """
---
module: foo
author:
    - "Ansible Core Team"
    - "Someone else (@ansible)"
version_added: "2.0.0"
short_description: Do some foo O(bar)
description:
    - Does some foo on the remote host.
    - Whether foo is magic or not has not yet been determined.
options:
    foo:
        description: The foo source.
        type: str
        required: true
    bar:
        description:
          - A bar.
          - Independent from O(foo).
          - Do not confuse with RV(bar).
        type: list
        elements: int
        aliases:
          - baz
    subfoo:
        description: Some recursive foo.
        version_added: 2.0.0
        type: dict
        suboptions:
            foo:
                description:
                    - A sub foo.
                    - Whatever.
                    - Also required when O(subfoo) is specified when O(foo=bar) or V(baz).
                type: str
                required: true

requirements:
    - Foo on remote.

attributes:
    check_mode:
        description: Can run in check_mode and return changed status prediction without modifying target
        support: full
    diff_mode:
        description: Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode
        support: full
    platform:
        description: Target OS/families that can be operated against
        support: N/A
        platforms: posix
    action_group:
        description: Use C(group/ns2.col.foo_group) in C(module_defaults) to set defaults for this module.
        support: full
        membership:
          - ns2.col.foo_group

seealso:
    - module: ns2.col.foo2
    - module: ns2.col.foo3  # does not exist
    - plugin: ns2.col.foo
      plugin_type: lookup
"""

EXAMPLES = """
- name: Do some foo
  ns2.col.foo:
    foo: '{{ foo }}'
    bar:
      - 1
      - 2
      - 3
    subfoo:
      foo: hoo!
"""

RETURN = """
bar:
    description:
      - Some bar.
      - Referencing myself as RV(bar).
      - Do not confuse with O(bar).
    returned: success
    type: str
    sample: baz
"""

from ansible.module_utils.basic import AnsibleModule


def main():
    module = AnsibleModule(
        argument_spec=dict(
            foo=dict(type="str", required=True),
            bar=dict(type="list", elements="int", aliases=["baz"]),
            subfoo=dict(type="dict", options=dict(foo=dict(type="str", required=True))),
        ),
        supports_check_mode=True,
    )
    module.exit_json(bar="baz")


if __name__ == "__main__":
    main()
