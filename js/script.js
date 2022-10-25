window.onload = function() {
    // let text = document.querySelectorAll('table tbody tr td:first-child, table tbody tr td:nth-child(5), table tbody tr td:nth-child(6)');
    let txtchoice = '';
    let startbtn = document.getElementById('startbtn');
    let settingsbtn = document.getElementById('settingsbtn');
    let settingstab = document.getElementById('settingstab');
    let chkboxs = document.getElementsByName('chkbox');
    settingsbtn.onclick = function() {
        settingstab.classList.toggle('hiddenClass');
    };

    
    let txtchoicetemp;

    startbtn.onclick = function() {
        txtchoice = '';
        for (let i = 0; i < chkboxs.length; i++) {
            if (chkboxs[i].checked == true && i == 0) {
                if (txtchoice != '') {
                    txtchoice += ', table tbody tr td:nth-child(1)'
                } else {
                    txtchoice += 'table tbody tr td:nth-child(1)'
                }
            } else if (chkboxs[i].checked == true && i == 1) {
                if (txtchoice != '') {
                    txtchoice += ', table tbody tr td:nth-child(2)'
                } else {
                    txtchoice += 'table tbody tr td:nth-child(2)'
                }
            } else if (chkboxs[i].checked == true && i == 2) {
                if (txtchoice != '') {
                    txtchoice += ', table tbody tr td:nth-child(3)'
                } else {
                    txtchoice += 'table tbody tr td:nth-child(3)'
                }
            } else if (chkboxs[i].checked == true && i == 3) {
                if (txtchoice != '') {
                    txtchoice += ', table tbody tr td:nth-child(4)'
                } else {
                    txtchoice += 'table tbody tr td:nth-child(4)'
                }
            } else if (chkboxs[i].checked == true && i == 4) {
                if (txtchoice != '') {
                    txtchoice += ', table tbody tr td:nth-child(5)'
                } else {
                    txtchoice += 'table tbody tr td:nth-child(5)'
                }
            } else if (chkboxs[i].checked == true && i == 5) {
                if (txtchoice != '') {
                    txtchoice += ', table tbody tr td:nth-child(6)'
                } else {
                    txtchoice += 'table tbody tr td:nth-child(6)'
                }
            }
        }
        // console.log(txtchoice);
        // console.log(txtchoicetemp);
        let text = startbtn.innerHTML == 'Start Test' ? document.querySelectorAll(txtchoice) : document.querySelectorAll(txtchoicetemp);
        txtchoicetemp = startbtn.innerHTML == 'Start Test' ? txtchoice : '';
        // console.log(txtchoicetemp);
        
        // if (startbtn.innerHTML == 'Start Test') {
        //     // txtchoicetemp = txtchoice;
        //     console.log(txtchoicetemp);
        //     text = document.querySelectorAll(txtchoice);
        // } else {
        //     text = document.querySelectorAll(txtchoicetemp);
        //     console.log(txtchoicetemp);
        // }
        for (let i = 0; i < text.length; i++) {
            // if (text[i].style.visibility == 'hidden') {
            // 	text[i].style.visibility = 'visible';
            // } else {
            // 	text[i].style.visibility = 'hidden';
            // }
            text[i].classList.toggle('hiddenClass');
        }
        if (startbtn.innerHTML == 'Start Test') {
            startbtn.innerHTML = 'End Test';
            // testbtn.style.backgroundColor = '#ff4a4a';
            startbtn.classList.add('red');
        } else {
            startbtn.innerHTML = 'Start Test'
            startbtn.classList.remove('red');
        }
        if (startbtn.innerHTML == 'Start Test') {
            // txtchoicetemp = '';
        } else {

        }
    };
}