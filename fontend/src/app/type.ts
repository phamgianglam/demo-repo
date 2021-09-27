import { UUID } from 'angular2-uuid';

enum wardEnum {
    ward_a = "ward 1",
    ward_b = "ward 2",
    ward_c = "ward 3",
    ward_d = "ward 4",
    ward_e = "ward 5",
    ward_f = "ward 6",
    ward_g = "ward 7"
}
enum districtEnum {
    district_1 = "distrcit 1",
    district_2 = "distrcit 2",
    district_3 = "distrcit 3",
    district_4 = "distrcit 4",
    district_5 = "distrcit 5",
    district_6 = "distrcit 6",
    district_7 = "distrcit 7"

}


export class User {
    id: string = "string";
    name: string = "string";
    phone: string = "string";
    citizenId: string = "string";
    address: string = "string";
    district: districtEnum = districtEnum.district_1;
    ward: wardEnum = wardEnum.ward_a;
    vip: boolean = false
}