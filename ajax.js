"use strict";

$.ajax({
    type: 'GET',
    cache: false,
    url: 'https://leetcode-stats-api.herokuapp.com/RotRaider',
    dataType: "json",
    success: function(data) {
        var easy_perc = data.easySolved / data.totalEasy * 100
        var easy_count = data.easySolved
        $('#easycount').append(`<h5>Easy</h5><div class=\"progress\">
                                <div class=\"progress-bar progress-bar-striped progress-bar-animated bg-success\" role=\"progressbar\" aria-valuenow=\"` + String(easy_perc) + `
                                \" aria-valuemin=\"0\" aria-valuemax=\"100\" style=\"width: ` + String(easy_perc) + `%\"></div>` + String(easy_count) + "</div>")
    }
});

$.ajax({
    type: 'GET',
    cache: false,
    url: 'https://leetcode-stats-api.herokuapp.com/RotRaider',
    dataType: "json",
    success: function(data) {
        var medium_perc = data.mediumSolved / data.totalMedium * 100
        var medium_count = data.mediumSolved
        $('#mediumcount').append(`<h5>Medium</h5><div class=\"progress\">
                                <div class=\"progress-bar progress-bar-striped progress-bar-animated bg-warning\" role=\"progressbar\" aria-valuenow=\"` + String(medium_perc) + `
                                \" aria-valuemin=\"0\" aria-valuemax=\"100\" style=\"width: ` + String(medium_perc) + `%\"></div>` + String(medium_count) + "</div>")
    }
});

$.ajax({
    type: 'GET',
    cache: false,
    url: 'https://leetcode-stats-api.herokuapp.com/RotRaider',
    dataType: "json",
    success: function(data) {
        var hard_perc = data.hardSolved / data.totalHard * 100
        var hard_count = data.hardSolved
        $('#hardcount').append(`<h5>Hard</h5><div class=\"progress\">
                                <div class=\"progress-bar progress-bar-striped progress-bar-animated bg-danger\" role=\"progressbar\" aria-valuenow=\"` + String(hard_perc) + `
                                \" aria-valuemin=\"0\" aria-valuemax=\"100\" style=\"width: ` + String(hard_perc) + `%\"></div>` + String(hard_count) + "</div>")
    }
});

$.ajax({
    type: "GET",
    cache: false,
    url: "https://api.github.com/repos/Sadamingh/code-tracker/git/trees/main",
    headers: {'Authorization': '${{ secrets.TOKEN }}' },
    dataType: "json",
    success: function(data) {
        var arr = data.tree
        for(var idx in arr) {
            if(arr[idx].type === "tree") {
                let title = "";
                let titleArr = arr[idx].path.split("-")
                let titleNum = titleArr[0]
                titleArr.shift()
                for(var titleIdx in titleArr) {
                    title += titleArr[titleIdx].charAt(0).toUpperCase() + titleArr[titleIdx].slice(1) + " "
                }
                $('#content').append("<div class=\"col-2\"><span class=\"badge text-bg-primary\">" + titleNum + 
                 "</span> </div><div class=\"col-8\"> " + title + "</div> <div class=\"col-2\">" + 
                 "<a href=\"https://github.com/Sadamingh/code-tracker/blob/main/" + 
                 arr[idx].path + "\">link</a></div>")
            }
        }
    }
});

$("#click-me").click(function () {

    $.ajax({
        success: function (data) {                               
            console.log(data);   
            $('#info-modal').addClass("show"); 
        },
        async: true
    });    
});
    
$(".modal-dialog .close").click(function(){
    $(this).closest(".modal-dialog").removeClass("show"); 
});