$(document).ready(function () {
	$(".open").click(function () {


	   $(".open").hide();
	   $(".close").fadeIn();

	   $(".header_inner .menu").toggle("500", "swing");
	   //  $(".head_side").css("padding-top", "200px");

	})
 });


 $(document).ready(function () {
	$(".close").click(function () {


	   $(".close").hide();
	   $(".open").fadeIn();

	   $(".header_inner .menu").toggle("slow");
	   //  $(".head_side").css("padding-top", "200px");

	})
 });