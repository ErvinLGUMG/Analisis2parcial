import { Component, OnInit } from '@angular/core';
import { LoginService } from '../../service/login.service';
import { Router } from '@angular/router';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';

@Component({
    selector: 'app-signup',
    templateUrl: './signup.component.html',
    // styleUrls: ['./signup.component.scss']
    providers: [LoginService]
})
export class SignupComponent implements OnInit {
    private loginService: LoginService;
    private router: Router;
    generalForm: FormGroup;
    private formBuilder: FormBuilder;
    test : Date = new Date();
    focus;
    focus1;
    user: any = {'username': '', 'password': ''}

    constructor(
        router: Router,
        loginService: LoginService,
        formBuilder: FormBuilder
    ) {
        this.router = router;
        this.loginService = loginService;
        this.formBuilder = formBuilder;
     }

    ngOnInit() {
        this.generalForm = this.formBuilder.group({
            username: [null],
            password: [null],
          });
    }

    login() {
        const data: any = this.generalForm.value;
        this.loginService.login(data).subscribe (
            Response => {
                console.log("si hace login");
                this.router.navigate(['/home']);
            },
            error => {
                console.log(error)
            }
        );
    }
}
