import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, ParamMap } from '@angular/router'
import { UserService } from '../../../service/user.service'
import { User } from '../../../type'

@Component({
  selector: 'app-user-form',
  templateUrl: './user-form.component.html',
  styleUrls: ['./user-form.component.css']
})
export class UserFormComponent implements OnInit {
  myId: string | null = null;
  myUser = new User()
  constructor(private route: ActivatedRoute, private userService: UserService) {

  }

  ngOnInit() {

    this.route.paramMap.subscribe((params: ParamMap) => {
      let id = this.route.snapshot.paramMap.get('id')
      console.log("i am here", id)
      this.myId = id
      if (typeof this.myId === "string") {
        this.initUser(this.myId)
      }
    })
  }


  async initUser(id: string) {
    this.myUser = await this.userService.getUser(<string>id).then();
    console.warn(this.myUser)
  }

}
