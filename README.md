# iris-project

## How to update the site

Updating is just a matter of commiting and pushing your changes. Github-pages will automatically observe the change and in a matter of seconds the main home-page will be updated. 

## How to add publications

To add a new publication find
```html
    <dl class="ref">
```
which is the datalist containing references to publications. A publication consists of two tags, a *dt* tag containing the title and a *dd* tag containing authors and links. Copy a paper-section like the following:

```html
          <dt>Iris: Monoids and Invariants as an Orthogonal Basis for Concurrent Reasoning</dt>
          <dd>
            <div class="entry">
              Ralf Jung, David Swasey, Filip Sieczkowski, Kasper Svendsen, Aaron Turon, Lars Birkedal, and Derek Dreyer<br />
              <small class="text-muted">In POPL 2015: ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages, Mumbai, India</small>
              <div class="buttons">
                <a href="http://plv.mpi-sws.org/iris/paper.pdf" class="btn btn-outline-primary btn-sm">.pdf</a>
                <a href="http://plv.mpi-sws.org/iris/appendix.pdf" class="btn btn-outline-primary btn-sm">technical appendix</a>
                <a href="http://dl.acm.org/citation.cfm?doid=2676726.2676980" class="btn btn-outline-primary btn-sm">publisher's site</a>
              </div>
            </div>
          </dd>
```

and insert it into the top right below:

```html
        <dl class="ref">
```

To add links to the paper, to techinical appendices, repositories etc. find:

```html
	<div class="buttons">
```

One can add a new link simple by adding another anchor-entry to the div:

```html
        <a href="http://some.link/to/a.pdf" class="btn btn-outline-primary btn-sm">name for link</a>
```