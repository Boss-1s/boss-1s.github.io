<head><style>.markdown-alert{padding:.5rem 1rem;margin-bottom:1rem;color:inherit;border-left:.25em solid #30363d}.markdown-alert>:first-child{margin-top:0}.markdown-alert>:last-child{margin-bottom:0}.markdown-alert .markdown-alert-title{display:flex;font-weight:500;align-items:center;line-height:1}.markdown-alert svg{margin-right:.5rem!important}.markdown-alert svg path{fill:currentColor}.markdown-alert.markdown-alert-note{border-left-color:#4493f8}.markdown-alert.markdown-alert-note .markdown-alert-title{color:#4493f8}.markdown-alert.markdown-alert-important{border-left-color:#ab7df8}.markdown-alert.markdown-alert-important .markdown-alert-title{color:#ab7df8}.markdown-alert.markdown-alert-warning{border-left-color:#9e6a03}.markdown-alert.markdown-alert-warning .markdown-alert-title{color:#d29922}.markdown-alert.markdown-alert-tip{border-left-color:#238636}.markdown-alert.markdown-alert-tip .markdown-alert-title{color:#3fb950}.markdown-alert.markdown-alert-caution{border-left-color:#da3633}.markdown-alert.markdown-alert-caution .markdown-alert-title{color:#f85149}</style></head>var idx = lunr(function () {
  this.field('title')
  this.field('excerpt')
  this.field('categories')
  this.field('tags')
  this.ref('id')

  this.pipeline.remove(lunr.trimmer)

  for (var item in store) {
    this.add({
      title: store[item].title,
      excerpt: store[item].excerpt,
      categories: store[item].categories,
      tags: store[item].tags,
      id: item
    })
  }
});

$(document).ready(function() {
  $('input#search').on('keyup', function () {
    var resultdiv = $('#results');
    var query = $(this).val().toLowerCase();
    var result =
      idx.query(function (q) {
        query.split(lunr.tokenizer.separator).forEach(function (term) {
          q.term(term, { boost: 100 })
          if(query.lastIndexOf(" ") != query.length-1){
            q.term(term, {  usePipeline: false, wildcard: lunr.Query.wildcard.TRAILING, boost: 10 })
          }
          if (term != ""){
            q.term(term, {  usePipeline: false, editDistance: 1, boost: 1 })
          }
        })
      });
    resultdiv.empty();
    resultdiv.prepend('<p class="results__found">'+result.length+' Result(s) found</p>');
    for (var item in result) {
      var ref = result[item].ref;
      if(store[ref].teaser){
        var searchitem =
          '<div class="list__item">'+
            '<article class="archive__item" itemscope itemtype="https://schema.org/CreativeWork">'+
              '<h2 class="archive__item-title" itemprop="headline">'+
                '<a href="'+store[ref].url+'" rel="permalink">'+store[ref].title+'</a>'+
              '</h2>'+
              '<div class="archive__item-teaser">'+
                '<img src="'+store[ref].teaser+'" alt="">'+
              '</div>

'+
              '<p class="archive__item-excerpt" itemprop="description">'+store[ref].excerpt.split(" ").splice(0,20).join(" ")+'...</p>'+
            '</article>'+
          '</div>

';
      }
      else{
    	  var searchitem =
          '<div class="list__item">'+
            '<article class="archive__item" itemscope itemtype="https://schema.org/CreativeWork">'+
              '<h2 class="archive__item-title" itemprop="headline">'+
                '<a href="'+store[ref].url+'" rel="permalink">'+store[ref].title+'</a>'+
              '</h2>'+
              '<p class="archive__item-excerpt" itemprop="description">'+store[ref].excerpt.split(" ").splice(0,20).join(" ")+'...</p>'+
            '</article>'+
          '</div>

';
      }
      resultdiv.append(searchitem);
    }
  });
});
