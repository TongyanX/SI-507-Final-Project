function openShutManager(oSourceObj, oTargetObj, shutAble, oOpenTip, oShutTip){
    var sourceObj = typeof oSourceObj == "string" ? document.getElementById(oSourceObj) : oSourceObj;
    var targetObj = typeof oTargetObj == "string" ? document.getElementById(oTargetObj) : oTargetObj;
    var openTip = oOpenTip || "";
    var shutTip = oShutTip || "";
    if(targetObj.style.display != "none"){
       if(shutAble) return;
       targetObj.style.display = "none";
       if(openTip && shutTip){
        sourceObj.innerHTML = shutTip;
       }
    } else {
       targetObj.style.display = "block";
       if(openTip && shutTip){
        sourceObj.innerHTML = openTip;
       }
    }
};


$.fn.dataTable.ext.type.order["ranking-pre"] = function (x) {
    if (x == "231 - 300"){
        return 231;
    }
    else if (x == "Unranked"){
        return 232;
    }
    else {
        return parseInt(x);
    };
};


$.fn.dataTable.ext.type.order["blank-asc"] = function (x, y) {
    if (x == null){
        if (y == null){
            return 0;
        }
        else {
            return 1;
        };
    }
    else if (y == null){
        return -1;
    }
    else {
        return x - y;
    };
};


$.fn.dataTable.ext.type.order["blank-desc"] = function (x, y) {
    if (x == null){
        if (y == null){
            return 0;
        }
        else {
            return 1;
        };
    }
    else if (y == null){
        return -1;
    }
    else {
        return y - x;
    };
};


function univ_table(){
    openShutManager("hidden-bar", "hidden-box", false,
        "Click to hide state checkboxes", "Click to show state checkboxes");

    var id_array = new Array();
    $("input[name='state']:checked").each(function(){
        id_array.push($(this).attr("id"));
    });
    var id_str = id_array.join(",");

    table_obj.destroy();
    table_obj = $("#data-table").DataTable({
        ajax: {
            url: "/univ/?state=" + id_str,
            dataSrc: ""
        },
        columns: [
            {
                data: "Name",
                title: "Name",
                width: "40px",
                className: "dt-head-center dt-body-center"
            },
            {
                data: "Ranking",
                title: "Ranking",
                width: "40px",
                className: "dt-head-center dt-body-center"
            },
            {
                data: "State",
                title: "State",
                width: "30px",
                className: "dt-head-center dt-body-center"
            },
            {
                data: "City",
                title: "City",
                width: "50px",
                className: "dt-head-center dt-body-center"
            },
            {
                data: "Type",
                title: "Type",
                width: "40px",
                className: "dt-head-center dt-body-center"
            },
            {
                data: "FoundYear",
                title: "Found Year",
                width: "40px",
                className: "dt-head-center dt-body-center"
            },
            {
                data: "Endowment",
                title: "Endowment (Million $)",
                width: "60px",
                className: "dt-head-center dt-body-center"
            },
            {
                data: "TuitionAndFeesInState",
                title: "In State",
                width: "70px",
                className: "dt-head-center dt-body-center"
            },
            {
                data: "TuitionAndFeesOutOfState",
                title: "Out State",
                width: "70px",
                className: "dt-head-center dt-body-center"
            },
            {
                data: "Enrollment",
                title: "Enrollment",
                width: "60px",
                className: "dt-head-center dt-body-center"
            },
            {
                data: "MedianStartingSalary",
                title: "Starting Salary",
                width: "60px",
                className: "dt-head-center dt-body-center"
            },
            {
                data: "StudentFacultyRatio",
                title: "Student / Faculty",
                width: "60px",
                className: "dt-head-center dt-body-center"
            },
            {
                data: "FemalePercentage",
                title: "Female %",
                width: "60px",
                className: "dt-head-center dt-body-center"
            }
        ],
        columnDefs: [
            {
                targets: [5, 6, 7, 8, 9, 10, 11, 12],
                type: "blank"
            },
            {
                targets: 1,
                type: "ranking"
            }
        ],
        pageLength: 50,
        lengthMenu: [[20, 50, 100, 200, -1], [20, 50, 100, 200, "ALL"]],
        scrollY: 380
    });
};


function gdp_table(){
    openShutManager("hidden-bar", "hidden-box", false,
        "Click to hide state checkboxes", "Click to show state checkboxes");

    var id_array = new Array();
    $("input[name='state']:checked").each(function(){
        id_array.push($(this).attr("id"));
    });
    var id_str = id_array.join(",");

    table_obj.destroy();
    table_obj = $("#data-table").DataTable({
        ajax: {
            url: "/gdp/?state=" + id_str,
            dataSrc: ""
        },
        columns: [
            {
                data: "Name",
                title: "Name",
                width: "200px",
                className: "dt-head-center dt-body-center"
            },
            {
                data: "Y1997",
                title: "1997",
                width: "40px",
                className: "dt-head-center dt-body-center"
            },
            {
                data: "Y1998",
                title: "1998",
                width: "40px",
                className: "dt-head-center dt-body-center"
            },
            {
                data: "Y1999",
                title: "1999",
                width: "40px",
                className: "dt-head-center dt-body-center"
            },
            {
                data: "Y2000",
                title: "2000",
                width: "40px",
                className: "dt-head-center dt-body-center"
            },
            {
                data: "Y2001",
                title: "2001",
                width: "40px",
                className: "dt-head-center dt-body-center"
            },
            {
                data: "Y2002",
                title: "2002",
                width: "40px",
                className: "dt-head-center dt-body-center"
            },
            {
                data: "Y2003",
                title: "2003",
                width: "40px",
                className: "dt-head-center dt-body-center"
            },
            {
                data: "Y2004",
                title: "2004",
                width: "40px",
                className: "dt-head-center dt-body-center"
            },
            {
                data: "Y2005",
                title: "2005",
                width: "40px",
                className: "dt-head-center dt-body-center"
            },
            {
                data: "Y2006",
                title: "2006",
                width: "40px",
                className: "dt-head-center dt-body-center"
            },
            {
                data: "Y2007",
                title: "2007",
                width: "40px",
                className: "dt-head-center dt-body-center"
            },
            {
                data: "Y2008",
                title: "2008",
                width: "40px",
                className: "dt-head-center dt-body-center"
            },
            {
                data: "Y2009",
                title: "2009",
                width: "40px",
                className: "dt-head-center dt-body-center"
            },
            {
                data: "Y2010",
                title: "2010",
                width: "40px",
                className: "dt-head-center dt-body-center"
            },
            {
                data: "Y2011",
                title: "2011",
                width: "40px",
                className: "dt-head-center dt-body-center"
            },
            {
                data: "Y2012",
                title: "2012",
                width: "40px",
                className: "dt-head-center dt-body-center"
            },
            {
                data: "Y2013",
                title: "2013",
                width: "40px",
                className: "dt-head-center dt-body-center"
            },
            {
                data: "Y2014",
                title: "2014",
                width: "40px",
                className: "dt-head-center dt-body-center"
            },
            {
                data: "Y2015",
                title: "2015",
                width: "40px",
                className: "dt-head-center dt-body-center"
            },
            {
                data: "Y2016",
                title: "2016",
                width: "40px",
                className: "dt-head-center dt-body-center"
            }
        ],
        pageLength: 20,
        lengthMenu: [[20, 50, -1], [20, 50, "ALL"]],
        scrollY: 380
    });
};
