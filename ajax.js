"use strict";

$.ajax({
    type: 'GET',
    cache: false,
    url: 'https://leetcode-stats-api.herokuapp.com/RotRaider',
    dataType: "json",
    // beforeSend: function(){
    //     $('#loading-image').show();
    // },
    // complete: function(){
    //     $('#loading-image').hide();
    // },
    success: function(data) {
        $('#output').append(data.status + "<br/>" + data.ranking)
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
                $('#content').append("<span class=\"badge text-bg-primary\">" + titleNum + "</span> " + title)
                $('#content').append("</br>")
            }
        }
    }
});