function bar(){
    document.getElementById("hidden-bar").style.display="block";
};


function bar_cancel(){
    document.getElementById("hidden-bar").style.display="none";
};


function line(){
    document.getElementById("hidden-line").style.display="block";
};


function line_cancel(){
    document.getElementById("hidden-line").style.display="none";
};


function bubble(){
    document.getElementById("hidden-bubble").style.display="block";
};


function bubble_cancel(){
    document.getElementById("hidden-bubble").style.display="none";
};


function scatter(){
    document.getElementById("hidden-scatter").style.display="block";
};


function scatter_cancel(){
    document.getElementById("hidden-scatter").style.display="none";
};


function map(){
    document.getElementById("hidden-map").style.display="block";
};


function map_cancel(){
    document.getElementById("hidden-map").style.display="none";
};


function close_plot(){
    document.getElementById("plot-result").style.display="none";
};


function bar_plot(){
    var limit = $("#limit").val();

    $.ajax({
        url: "/plot/bar/",
        type: "get",
        data: "limit=" + limit,
        dataType: "text",
        success: function(callback) {
            document.getElementById("hidden-bar").style.display="none";
            document.getElementById("plot-result").style.display="block";
            $("#plot").html(callback);
        },
        fail: function() {
            alert("Failed!");
            document.getElementById("hidden-bar").style.display="none";
        }
    });
};


function line_plot(){
    var id_array = new Array();
    $("input[name='state']:checked").each(function(){
        id_array.push($(this).attr("id"));
    });
    var id_str = id_array.join(",");

    $.ajax({
        url: "/plot/line/",
        type: "get",
        data: "state=" + id_str,
        dataType: "text",
        success: function(callback) {
            document.getElementById("hidden-line").style.display="none";
            document.getElementById("plot-result").style.display="block";
            $("#plot").html(callback);
        },
        fail: function() {
            alert("Failed!");
            document.getElementById("hidden-line").style.display="none";
        }
    });
};


function histogram_plot(){
    $.ajax({
        url: "/plot/histogram/",
        type: "get",
        dataType: "text",
        success: function(callback) {
            document.getElementById("plot-result").style.display="block";
            $("#plot").html(callback);
        },
        fail: function() {
            alert("Failed!");
        }
    });
};


function bubble_plot(){
    var add_param = $("#add_param").val();

    $.ajax({
        url: "/plot/bubble/",
        type: "get",
        data: "add_param=" + add_param,
        dataType: "text",
        success: function(callback) {
            document.getElementById("hidden-bubble").style.display="none";
            document.getElementById("plot-result").style.display="block";
            $("#plot").html(callback);
        },
        fail: function() {
            alert("Failed!");
            document.getElementById("hidden-bubble").style.display="none";
        }
    });
};


function scatter_plot(){
    var x = $("#x").val();
    var y = $("#y").val();
    var cor = x + "," + y;

    $.ajax({
        url: "/plot/scatter/",
        type: "get",
        data: "cor=" + cor,
        dataType: "text",
        success: function(callback) {
            document.getElementById("hidden-scatter").style.display="none";
            document.getElementById("plot-result").style.display="block";
            $("#plot").html(callback);
        },
        fail: function() {
            alert("Failed!");
            document.getElementById("hidden-scatter").style.display="none";
        }
    });
};


function map_plot(){
    var state = $("#state").val();

    $.ajax({
        url: "/plot/map/",
        type: "get",
        data: "state=" + state,
        dataType: "text",
        success: function(callback) {
            document.getElementById("hidden-map").style.display="none";
            document.getElementById("plot-result").style.display="block";
            $("#plot").html(callback);
        },
        fail: function() {
            alert("Failed!");
            document.getElementById("hidden-map").style.display="none";
        }
    });
};
