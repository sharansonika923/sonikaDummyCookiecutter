import os
import json
os.system("ng new {{cookiecutter.angularprojectname}}")
os.chdir("{{cookiecutter.angularprojectname}}")
items="{{cookiecutter.angularcomponents}}"
listofcomponents= json.loads(items)

print(listofcomponents)
# os.system("ng generate component signup")
# routes = """
# import { NgModule } from '@angular/core';
# import { Routes, RouterModule } from '@angular/router';
# import { LoginComponent } from './login/login.component';
# import { SignupComponent } from './signup/signup.component';

# const routes: Routes = [
#   { path: 'login', component: LoginComponent },
#   { path: 'signup', component: SignupComponent }
# ];

# @NgModule({
#   imports: [RouterModule.forRoot(routes)],
#   exports: [RouterModule]
# })
# export class AppRoutingModule { }
# """

# with open("src/app/app-routing.module.ts", "w") as f:
#     f.write(routes)
