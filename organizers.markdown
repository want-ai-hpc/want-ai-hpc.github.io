---
layout: page
title: Organizers
permalink: /neurips2023/organizers
---

<style>
.row {
  display: flex;
}

/* Create three equal columns that sits next to each other */
.column {
  flex: 33.33%;
  padding: 15px;
  text-align: center;
}


/* .columns {
  float: left;
  position: relative;
  margin-right: 20px;
} */


img {
  border-radius: 50%;
}

summary {
    font-size: large
}

ul {
  columns: 2;
  -webkit-columns: 2;
  -moz-columns: 2;
}
</style>

<div class="row">
  <div class="column">
    <img src="{{site.url}}/assets/juliaG.jpeg" title="Julia Gusak" width="100%" />
    <figcaption>
    <details>
    <summary>
    <b>Julia Gusak</b> <br /><em>INRIA</em>
    </summary>
    <a href="https://scholar.google.com/citations?hl=en&user=QriHoq4AAAAJ&view_op=list_works&sortby=pubdate">Publications</a>
    <a href="https://juliagusak.github.io/about/">Website</a>
    </details>
    </figcaption>
  </div>

  <div class="column">
    <img src="{{site.url}}/assets/jeanK.jpeg" title="Jean Kossaifi " width="100%" />
    <figcaption>
    <details>
    <summary>
    <b>Jean Kossaifi</b> <br /><em>NVIDIA</em>
    </summary>
    <a href="https://scholar.google.com/citations?hl=en&user=hJS2TXwAAAAJ&view_op=list_works&sortby=pubdate">Publications</a>
    <a href="http://jeankossaifi.com/">Website</a>
    </details>
    </figcaption>
  </div>

  <div class="column">
    <img src="{{site.url}}/assets/Alena.jpg" title="Alena Shilova" width="100%" />
    <figcaption>
    <details>
    <summary>
    <b>Alena Shilova</b> <br /><em>INRIA</em>
    </summary>
    <a href="https://scholar.google.com/citations?hl=en&user=hiHDpfgAAAAJ&view_op=list_works">Publications</a>
    <a href="https://aleshi94.github.io/home/">Website</a>
    </details>
    </figcaption>
  </div>
</div>

<div class="row">
  <div class="column">
    <img src="{{site.url}}/assets/cristiana.gif" title="Cristiana Bentes" width="100%" />
    <figcaption>
    <details>
    <summary>
    <b>Cristiana Bentes</b> <br /><em>Federal University of Rio de Janeiro</em>
    </summary>
    <a href="https://dblp.org/pid/b/CristianaBentes.html">Publications</a>
    <!-- <a href="">Website</a> -->
    </details>
    </figcaption>
  </div>
  <div class="column">
    <img src="{{site.url}}/assets/Anima.jpeg" title="Anima Anandkumar" width="100%" />
    <figcaption>
    <details>
    <summary>
    <b>Anima Anandkumar</b> <br /><em>NVIDIA, Caltech</em>
    </summary>
    <a href="https://scholar.google.com/citations?user=bEcLezcAAAAJ&hl=en&oi=ao">Publications</a>
    <a href="http://tensorlab.cms.caltech.edu/users/anima/">Website</a>
    </details>
    </figcaption>
  </div>
  <div class="column">
    <img src="{{site.url}}/assets/OlivierB.jpeg" title="Olivier Beaumont" width="100%" />
    <figcaption>
    <details>
    <summary>
    <b>Olivier Beaumont</b> <br /><em>INRIA</em>
    </summary>
    <a href="https://scholar.google.com/citations?hl=en&user=XT007NgAAAAJ">Publications</a>
    <!-- <a href="">Website</a> -->
    </details>
    </figcaption>
  </div>
</div>


<div class="row">
  <div class="column">
    <img src="{{site.url}}/assets/roccoS.png" title="Rocco Sedona" width="33%" height="80%"/>
    <figcaption>
    <details>
    <summary>
    <b>Rocco Sedona</b> <br /><em> Jülich Supercomputing Centre, Forschunszentrum Jülich</em>
    </summary>
    <a href="https://scholar.google.com/citations?hl=de&user=nuFMOpYAAAAJ&view_op=list_works&sortby=pubdate">Publications</a>
    <!-- <a href="">Website</a> -->
    </details>
    </figcaption>
  </div>
</div>


## Area Chairs

- Adrian Bulat (Researcher, Samsung AI Cambridge & Technical University of Iasi)
- Boris Bonev (Research Scientist, NVIDIA)
- Maxim Panov (Assistant Professor, Mohamed bin Zayed University of Artificial Intelligence)
- Riad Akrour (Research Scientist, INRIA)
- Saurav Muralidharan (Researcher, NVIDIA)
- Tao Lin (Assistant Professor, Westlake University)




## Reviewers

<!-- {% assign row = site.data.authors[0] %}
{{ row | inspect }} -->

<!-- <table>
  {% for row in site.data.filtered %}

    {% tablerow pair in row %}
      {{ pair[1] }}
    {% endtablerow %}
  {% endfor %}
</table> -->

<ul>
{% for elem in site.data.filtered %}
  <li>
      {{ elem.name }} ({{ elem.company }})
  </li>
{% endfor %}
</ul>