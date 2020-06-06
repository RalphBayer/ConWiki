function save_article()
{
    // Get the textareas in create.html.
    var title     = document.getElementById('title')
    var main      = document.getElementById('main')
    var side_text = document.getElementById('side_text')

    // Create and send a json object.
    var entry = {
                    title: title.value,
                    main: main.value,
                    side_text: side_text.value
                }

    fetch('http://127.0.0.1:5000/save_article',
         {
             method: 'POST',
             credentials: 'include',
             body: JSON.stringify(data),
             cache: 'no-cache',
             headers: new Headers({
                                      'content-type': 'application/json'
                                 })
         })
}
