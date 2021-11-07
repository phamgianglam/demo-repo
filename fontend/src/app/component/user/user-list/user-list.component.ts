import { Component, OnChanges, OnInit } from '@angular/core';
import { UserService } from '../../../service/user.service'
import { User } from '../../../type'
import { Router } from '@angular/router'
@Component({
  selector: 'app-user-list',
  templateUrl: './user-list.component.html',
  styleUrls: ['./user-list.component.css']
})
export class UserListComponent implements OnInit {

  userList: User[] = []
  constructor(private userService: UserService, private router: Router) {

  }

  async deleteUser(id: string) {
    console.log(id)
    await this.userService.deleteUser(id)
    this.getUser()
  }

  ngOnInit(): void {
    this.getUser()
  }

  async getUser() {
    this.userList = await this.userService.getUsers().then()
    console.log(this.userList)

  }

  onSelect(item: string) {
    console.log(item)
    this.router.navigate(['/userDetail', item]);
    console.log(item)
  }

}
