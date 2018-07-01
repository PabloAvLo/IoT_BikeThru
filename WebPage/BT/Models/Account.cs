using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.ComponentModel.DataAnnotations;

namespace BT.Models
{
    public class Account
    {
        [Required]
        [MaxLength(80)]
        public string FullName { get; set; }
        public string Carne { get; set; }
        public string Email { get; set; }
        public string Password { get; set; }
        public int CI { get; }
        public int CO { get; }
    }
}