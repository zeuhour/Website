function ajax(data, method, url){
    let xhr = new XMLHttpRequest();
    xhr.open(method, url);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.send(data);
    xhr.onreadystatechange = function(){
        if(xhr.readyState==4 && xhr.status==200){
            // do something.
            window.alert(xhr.responseText);
        }
            
    }
}