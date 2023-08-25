$(function () {
    $("#button").on("click", function () {
        var name = $("#name").val()
        var address = $("#address").val()
        var email = $("#email").val()
        var dob = $("#dob").val()
        var gender = $("#gender").val()
        var password = $("#password").val()
        var password2 = $("#password2").val()

        if (containsNumbers(name) || containsSpecialChars(name)) {
            $("#warning").text("Invalid name");
        } else {
            if (name.length >= 3) {
                if (emailCheck(email)) {
                    if (address) {
                        if (dob) {
                            if (gender === "female" || gender === "male" || gender === "transgender" || gender === "non-binary") {
                                if (passwordCheck(password)) {
                                    if (password === password2) {
                                        window.location.href = "https://github.com/hereliesadvaith";
                                    } else {
                                        $("#password2p").text("Passwords don't match")
                                    }
                                } else {
                                    $("passwordp").text("invalid password")
                                }
                            } else {
                                $("#genderp").text("Please select gender")
                            }
                        } else {
                            $("#age").text("Please add you date of birth")
                        }
                    } else {
                        $("#addressp").text("Add your address")
                    }
                } else {
                    $("#emailp").text("Add email address")
                }
            } else {
                $("#namep").text("Add name");
            }
        };
    });
    $("#eye").on("click", function () {
        var classEye = $("#eye").attr("class")
        if (classEye === "pswd") {
            $("#password").attr("type", "text")
            $("#eye").attr("class", "text")
            $("#eye i").attr("class", "fa fa-eye-slash")
        } else {
            $("#password").attr("type", "password")
            $("#eye").attr("class", "pswd")
            $("#eye i").attr("class", "fa fa-eye")
        }
    });
    $("#eye2").on("click", function () {
        var classEye = $("#eye2").attr("class")
        if (classEye === "pswd") {
            $("#password2").attr("type", "text")
            $("#eye2").attr("class", "text")
            $("#eye2 i").attr("class", "fa fa-eye-slash")
        } else {
            $("#password2").attr("type", "password")
            $("#eye2").attr("class", "pswd")
            $("#eye2 i").attr("class", "fa fa-eye")
        }
    });
    $("#dob").on("change", function () {
        var dob = $("#dob").val()
        var age = getAge(dob)
        $("#age").text("Age: " + age)
    });

    $("#name").on("change", function () {
        var name = $("#name").val()
        if (containsNumbers(name) || containsSpecialChars(name)) {
            $("#namep").text("Invalid name")
        } else {
            if (name.length > 2) {
                $("#namep").text("")
            } else {
                $("#namep").text("Name is too short")
            }
        }
    })
    $("#email").on("change", function () {
        var email = $("#email").val()
        if (emailCheck(email)) {
            $("#emailp").text("")
        } else {
            $("#emailp").text("Invalid email address")
        }
    })
    $("#password").on("change", function () {
        var password = $("#password").val()
        passwordCheck(password)
    })
    $("#password2").on("change", function () {
        var password = $("#password").val()
        var password2 = $("#password2").val()
        if (password === password2) {
            $("#password2p").text("")
        } else {
            $("#password2p").text("Passwords don't match")
        }
    })

    $('#password, #password2').on("cut copy paste", function (e) {
        e.preventDefault();
    });

});

function containsSpecialChars(str) {
    const specialChars = /[`!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~]/;
    return specialChars.test(str);
}

function containsNumbers(str) {
    const digits = /\d/;
    return digits.test(str);
}

function emailCheck(str) {
    const specialChars = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    return specialChars.test(str)
}

function getAge(dateStr) {
    var today = new Date();
    var birthday = new Date(dateStr);
    var age = today.getFullYear() - birthday.getFullYear();
    var m = today.getMonth() - birthday.getMonth();
    if (m < 0 || m === 0 && today.getDate() < birthday.getDate()) {
        age--;
    };
    return age;
}

function hasUppercase(str) {
    const upperCaseChars = /[A-Z]/;
    return upperCaseChars.test(str)
}

function hasLowercase(str) {
    const lowerCaseChars = /[a-z]/;
    return lowerCaseChars.test(str)
}

function passwordCheck(str) {
    if (str.length > 7) {
        if (containsNumbers(str)) {
            if (containsSpecialChars(str)) {
                if (hasUppercase(str)) {
                    if (hasLowercase(str)) {
                        $("#passwordp").text("")
                        return true;
                    } else {
                        $("#passwordp").text("Password should have atleast one lowercase letter")
                    }
                } else {
                    $("#passwordp").text("Password should have atleast one uppercase letter")
                }
            } else {
                $("#passwordp").text("Password should have atleast one special character")
            }
        } else {
            $("#passwordp").text("Password should have atleast one number")
        }
    } else {
        $("#passwordp").text("Password too short")
    }
}