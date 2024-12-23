# ECU ATMAE Robotic's Website

## Accessibility
- `aria-current="page"` specifies the currently selected item of a `nav-bar`, which is used for [browser accessibility](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-current).
- `aria-selected="[true/false]"` specifies the currently selected pill of the pill widget. More info [here](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-selected).


## Updating the Site
### Adding a Project
1. A `button` and corresponding `div` must be added to the [projects](pages/projects.html) page inside the project pills.

2. The project should be detailed using the [project template](docs/templates/project_template.html).

### Updating the Navbar
1. Any changes to be made to the `navbar`, must be propagated to all pages that include the `navbar`.

### Propagating the Navbar
When adding the `navbar` to a new page, several considerations must be made:

1. If the new page is either under a new `nav-link`, then that `nav-link` must be made `nav-link active`, making the prior `nav-link active` into just a `nav-link`.

2. Likewise, `aria-current="page"` must be removed from the prior active `nav-link` and appended to the newly active `nav-link` as so: `class="nav-link active" aria-current="page"` 
     
3. Links are relative, and must be updated to account for what directory level they are on. 

## License
This repository is licensed under AGPL-3, refer to the [license](LICENSE) for more details.