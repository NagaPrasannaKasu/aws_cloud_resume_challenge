async function get_visitors() {
  
    let response = await fetch(
        "https://rnjzb7pf2y2qlamz5d3gjjncee0nxvgg.lambda-url.us-east-1.on.aws/"
    );
    let data = await response.json();
    console.log(data);
    document.getElementById("visitors").innerHTML = data;
    console.log(data)
    return data;
     
  }
get_visitors();
