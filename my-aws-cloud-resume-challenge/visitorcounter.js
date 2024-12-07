async function get_visitors() {  
    let response = await fetch("https://azzdfod28f.execute-api.us-east-1.amazonaws.com/default/VisitorCounter");
    let data = await response.json();
    console.log(data);
    document.getElementById("visitors").innerHTML = data;   
    return data;      
  }
get_visitors();
