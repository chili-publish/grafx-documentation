// Top-nav tab tweaks. Text-based tagging is needed because MkDocs writes
// relative hrefs: on pages inside a section, that section's tab href no
// longer contains its path, so CSS attribute selectors alone stop matching.
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".md-tabs__link").forEach(function (link) {
    var text = link.textContent.trim();

    // Stars badge on the Genie tab (styled in stylesheets/extra.css)
    if (/^(GraFx )?Genie\b/.test(text)) {
      link.classList.add("genie-tab");
    }
  });

  // Highlight the header quick link whose section is being viewed,
  // matching the active styling of the regular tabs.
  document.querySelectorAll(".md-header__links a").forEach(function (link) {
    var section = new URL(link.href, window.location.origin).pathname.split("/")[1];
    if (section && window.location.pathname.split("/")[1] === section) {
      link.classList.add("md-header__link--active");
    }
  });
});
