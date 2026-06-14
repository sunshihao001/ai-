# Accessibility Checklist

Use this for UI changes before merge.

## Keyboard and focus

- [ ] All interactive elements are reachable by keyboard.
- [ ] Focus order matches visual order.
- [ ] Focus state is visible.
- [ ] Modals/menus trap and restore focus correctly.

## Semantics

- [ ] Buttons are buttons, links are links.
- [ ] Form controls have labels and errors are associated.
- [ ] Headings are ordered and meaningful.
- [ ] Images/icons have appropriate alt text or are hidden from assistive tech.

## Visual

- [ ] Text contrast is acceptable.
- [ ] UI works at 200% zoom.
- [ ] Layout works on small viewport.
- [ ] Motion is not required for understanding.

## PR evidence

Paste tool output or manual notes:

```md
### Accessibility
- Keyboard:
- Screen reader/semantics:
- Contrast/zoom:
- Known limitations:
```
