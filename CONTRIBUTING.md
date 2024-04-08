# GraFx Documentation Contribution Guide

Welcome to the [GraFx Documentation](https://github.com/chili-publish/grafx-documentation) project! Your contribution is highly appreciated.

This guide highlights essential steps for setting up your project and offers a set of rules for contributing to the GraFx Documentation project. Adhering to our [Code of Conduct](CODE_OF_CONDUCT.md) helps foster a positive and collaborative environment. 

Please note that our project structure and guidelines take inspiration from [MDN Web Docs](https://github.com/mdn/content).

## Quickstart

Before you begin, make sure you have a [GitHub](https://github.com/) account. Then get acquainted with our [Code of Conduct](CODE_OF_CONDUCT.md).

For smooth navigation, consider reviewing these resources:
- [Markdown Basic Syntax](https://www.markdownguide.org/basic-syntax/): GraFx Documentation uses Markdown, a user-friendly lightweight markup language.
- [Writing Style Guide](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Writing_style_guide): Master the art of writing effective documentation with MDN Web Docs writing style guide.

For minor changes like a typo correction, see the [Simple Changes](#simple-changes) section. For advanced editing tasks, such as modifying multiple pages, consult the [Advanced Editing](#advanced-editing) section.

## Simple Changes

For small changes like a typo correction, use the GitHub UI. Follow these steps to propose a correction:

Let's consider a typo found on [GraFx Publisher](docs/GraFx-Publisher/index.md) intro page, and see how to propose a correction:

1. Navigate to the [GraFx Documentation repository](https://github.com/chili-publish/grafx-documentation).
2. Locate the source file (`docs/GraFx-Publisher/index.md`).
3. Click the pencil ✏️ icon in the upper right corner to enter edit mode.
   - If you're a first-time contributor, you will be prompted to "Fork this repository" and "Update your fork". Proceed accordingly.
4. After editing, click "Commit changes...".
5. Provide a commit message and description, then click "Propose changes".
6. You'll be redirected to a comparing changes page. Click "Create pull request".
7. Add comments explaining your changes, if necessary.
8. Finally, click "Create pull request".

Your pull request allows the project maintainers and the community to review your changes, give feedback, and suggest improvements. After review and approval, a CHILI employee will merge your changes into the `main` branch. See [Creating a Pull Request](#creating-a-pull-request) for more info.

Then congratulate yourself for contributing to the project 🎉.


## Advanced Editing

Advanced editing assumes familiarity with the command-line and `git`. If you're new to `git`, check out the [git-guides](https://github.com/git-guides).

For convenience, consider installing one of the following GitHub applications:
- [GitHub Desktop](https://docs.github.com/en/get-started/using-github/github-desktop): a desktop application providing a GUI experience.
- [GitHub CLI](https://docs.github.com/en/github-cli/github-cli/about-github-cli): a command-line tool for interacting with GitHub.

Before starting, [fork](https://github.com/chili-publish/grafx-documentation/fork) and [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) this project. Then, review the following sections:

- [Documentation Conventions](#documentation-page-conventions)
- [Modifying Documentation Structure](#modifying-documentation-structure)
- [Adding Images or Files](#adding-images-or-files)
- [Building And Testing](#building-and-testing)
- [Creating a Pull Request](#creating-a-pull-request)

### Documentation Page Conventions

When modifying existing pages or creating new ones, follow these conventions:

- `index.md` files contain the content of documentation pages.
- Each documentation page corresponds to a folder and `index.md` file.
  - Example: `index.md` for GraFx-Studio is in [`docs/GraFx-Studio`](docs/GraFx-Studio).
- Images referenced in an `index.md` file are stored in the same folder.
  - Example: `intro.png` for GraFx-Studio is in [`docs/GraFx-Studio`](docs/GraFx-Studio).
- Sub-pages are stored in sub-folders within a documentation page folder.
  - Example: [`docs/GraFx-Studio/overview/workspace-elements/index.md`](docs/GraFx-Studio/overview/workspace-elements/index.md).

### Modifying Documentation Structure

Modifying the documentation structure can involve adding, moving, or removing a page. Here are the generic steps you can follow:

1. Identify the page you want to add, move, or remove.
2. Add, move, or remove the directory and its associated `index.md` file.
3. Update `mkdocs.yml` to reflect your changes in the documentation navigation.

When modifying the documentation structure, it's best to [open an issue](https://github.com/chili-publish/grafx-documentation/issues/new) on GitHub to initiate a discussion. Any modification usually involves consensus from various parties, including CHILI publish documentation and product owners.

#### Example: Adding a New Page

To add a new page, such as 'JavaScript' under 'Concepts', follow these steps:

1. Create a new directory: `docs/GraFx-Studio/concepts/javascript/`.
2. Inside this directory, create an `index.md` file.
3. Update `mkdocs.yml` to add your page to the documentation navigation.

```yml
 - 'Frames & Timeline':              'GraFx-Studio/overview/timeline/index.md'
            - 'Stylekit': 'GraFx-Studio/overview/stylekits/index.md'
        - 'Concepts':
            - 'Frames': 'GraFx-Studio/concepts/frames/index.md'
            - 'Layers': 'GraFx-Studio/concepts/layers/index.md'
            - 'Layouts': 'GraFx-Studio/concepts/layouts/index.md'
            - 'Shapes': 'GraFx-Studio/concepts/shapes/index.md'
            - 'Variables': 'GraFx-Studio/concepts/variables/index.md'
            - 'Blend modes': 'GraFx-Studio/concepts/blendmodes/index.md'
            - 'Animation': 'GraFx-Studio/concepts/animation/index.md'
            - 'Stylekits': 'GraFx-Studio/concepts/stylekits/index.md'
            # ⬇️ Added the documentation page to the navigation⬇️
            - 'JavaScript': 'GraFx-Studio/concepts/javascript/index.md'
            - 'Keyboard Shortcuts': 'GraFx-Studio/concepts/shortcuts/index.md'
        - 'How to: Design documents':
            - 'Hello world': 'GraFx-Studio/guides/hello-world/index.md'
```

The current page order is based on perceived importance, which is subjective. If unsure, place the page where you deem a good fit. A maintainer will guide you if a different placement is necessary.

#### Adding release notes 

This repository is open for contribution, but as you will understand, releasenotes can only be pushed by CHILI publish staff members.
Pull requests from external sources will be denied.

The releasenotes uses a blog-style structure: each entry has its own page.
The pages can be found under docs/release-notes/releaseposts/[releasenote].md

![screensho](/docs/release-notes/releasenotesassets/releaseposts.png)

Where each file has the naming convention: yyyyMMddxx.md
- yyyy 4 digit year e.g. 2024
- MM 2 digit month e.g. 04
- dd 2 digit day e.g. 19 or 02
- xx 2 digit number to allow multiple releasenotes on 1 day.

This results in e.g. 2024040801.md

**Contents of the file**

``` markdown
---
draft: false
date: 2024-04-08
---

# Topic of the release

![rn_icon](/assets/icon-CHILI-GraFx.svg)

Contents of your Update

## New features

- Awesome new feature 1
- Awesome new feature 2

## Improvements

- Improvement 1
- Improvement 2

## Changes

- Thing you need to know!

```

The file starts with metadata holding
- draft status: true or false (true will not render in live guides)
- date: The publication date of the release note, formatted as: yyyy-MM-dd

The topic always starts with #

Followed by the relevant icon for the Platform or Application

| Application | Asset URL |
| ---- | ---- |
| CHILI GraFx | /assets/icon-CHILI-GraFx.svg|
| GraFx Data | /assets/icon-GraFx-Data.svg|
| GraFx Fonts | /assets/icon-GraFx-Fonts.svg|
| GraFx Genie | /assets/icon-Grafx-Genie.svg|
| GraFx Media | /assets/icon-GraFx-Media.svg|
| GraFx Publisher | /assets/icon-GraFx-Publisher.svg|
| GraFx Studio | /assets/icon-GraFx-Studio.svg|
| GraFx Stylekits | /assets/icon-GraFx-Stylekits.svg|

#### Example: Removing a Page

To remove a page, such as 'JavaScript' under 'Concepts', follow these steps:

1. Locate the directory: `docs/GraFx-Studio/concepts/javascript/`.
2. Delete the directory and update `mkdocs.yml` to remove the page, and any sub-pages, from the documentation navigation.

#### Example: Moving a Page

To move a page, such as 'JavaScript' under 'Concepts' to under `Guide`, follow these steps:

1. Locate the directory: `docs/GraFx-Studio/concepts/javascript/`.
2. Move the directory to the new location: `docs/GraFx-Studio/guide/javascript/`. Keep in mind that all sub-folders will be moved.
3. Update `mkdocs.yml` to change your page on the documentation navigation, as well as any sub-pages that were also under the original `docs/GraFx-Studio/concepts/javascript/`.

### Adding Images or Files

Images or files used on a page must be stored in the same folder as the page's `index.md`. Images must be under 1 MB and consist of original material or content freely available for commercial use without the need for attribution. Exceptions apply for content that depicts CHILI publish software.

For example, if we had a page 'JavaScript' under 'Concepts' found at the location `docs/GraFx-Studio/concepts/javascript/index.md` then all images for that page should be placed in `docs/GraFx-Studio/concepts/javascript/` folder.

If you need to reuse images across multiple pages, you need to add a copy of that image in each page's folder.

### Building And Testing

Refer to the [README.md](README.md) for how to build and test the project locally. Pull requests will be built automatically for review.

### Creating a Pull Request

When you've made your changes, [create a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request). A CHILI publish team member will review your changes and provide feedback.

Your pull request will be reviewed and approved before being merged into the `main` branch. You may be asked to answer questions or make changes during the review process. This a common part of the process.

## License

Any approved and merged content you submit will be subject to the terms of the project's [license](LICENSE). Ensure your contributions consist of original material, or content that is freely available for commercial use and requires no attribution. Exceptions apply for media content depicting CHILI publish software.
