
window.onload = function(){
    document.getElementById("main").onsubmit = function(){
        var post_data = "ips="+encodeURIComponent(document.getElementById("ips").value);
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '', true);
        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhr.setRequestHeader("Content-length", post_data.length);
        xhr.onreadystatechange = function(){
            if (xhr.readyState != 4) return;
            if (xhr.status == 200) {
                if (xhr.responseText == "1") {alert("There was an error."); return;}
                document.getElementById("output").innerHTML = xhr.responseText;
            } 
        }
        xhr.send(post_data);
        return false;
    }
}
