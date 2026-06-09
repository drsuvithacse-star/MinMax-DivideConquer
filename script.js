sync function findMaxMin(){

    let input =
        document.getElementById("numbers").value;

    let numbers =
        input.split(",").map(Number);

    let response = await fetch("/find",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({
            numbers:numbers
        })
    });

    let result = await response.json();

    document.getElementById("max").innerHTML =
        "Maximum Value : " + result.maximum;

    document.getElementById("min").innerHTML =
        "Minimum Value : " + result.minimum;
}
