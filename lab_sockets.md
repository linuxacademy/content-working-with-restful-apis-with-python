## Lab Description

The `socket` package in Python allows interactions between a server and many clients at a lower level than the typical TCP protocol or using the `requests` package.



## Additional Information and Resources (Scenario)

## Learning Objectives
#### Title
#### Description

## LAAS Settings
``` json
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Description": "Cloudformation template with 1 instance",
  "Mappings": {
    "SubnetConfig": {
      "VPC": {
        "CIDR": "10.0.0.0/16"
      },
      "Public1": {
        "CIDR": "10.0.1.0/24"
      }
    }
  },
  "Resources": {
    "VPC": {
      "Type": "AWS::EC2::VPC",
      "Properties": {
        "EnableDnsSupport": "true",
        "EnableDnsHostnames": "true",
        "CidrBlock": {
          "Fn::FindInMap": ["SubnetConfig", "VPC", "CIDR"]
        },
        "Tags": [
          {
            "Key": "Name",
            "Value": "LinuxAcademy"
          },
          {
            "Key": "Application",
            "Value": {
              "Ref": "AWS::StackName"
            }
          },
          {
            "Key": "Network",
            "Value": "VPC"
          }
        ]
      }
    },
    "PublicSubnet1": {
      "Type": "AWS::EC2::Subnet",
      "Properties": {
        "VpcId": {
          "Ref": "VPC"
        },
        "AvailabilityZone": {
          "Fn::Select": [
            "0",
            {
              "Fn::GetAZs": ""
            }
          ]
        },
        "CidrBlock": {
          "Fn::FindInMap": ["SubnetConfig", "Public1", "CIDR"]
        },
        "Tags": [
          {
            "Key": "Application",
            "Value": {
              "Ref": "AWS::StackName"
            }
          },
          {
            "Key": "Network",
            "Value": "Public1"
          }
        ]
      }
    },
    "InternetGateway": {
      "Type": "AWS::EC2::InternetGateway",
      "Properties": {
        "Tags": [
          {
            "Key": "Application",
            "Value": {
              "Ref": "AWS::StackName"
            }
          },
          {
            "Key": "Network",
            "Value": "Public"
          }
        ]
      }
    },
    "GatewayToInternet": {
      "Type": "AWS::EC2::VPCGatewayAttachment",
      "Properties": {
        "VpcId": {
          "Ref": "VPC"
        },
        "InternetGatewayId": {
          "Ref": "InternetGateway"
        }
      }
    },
    "PublicRouteTable": {
      "Type": "AWS::EC2::RouteTable",
      "Properties": {
        "VpcId": {
          "Ref": "VPC"
        },
        "Tags": [
          {
            "Key": "Application",
            "Value": {
              "Ref": "AWS::StackName"
            }
          },
          {
            "Key": "Network",
            "Value": "Public"
          }
        ]
      }
    },
    "PublicRoute": {
      "Type": "AWS::EC2::Route",
      "DependsOn": "GatewayToInternet",
      "Properties": {
        "RouteTableId": {
          "Ref": "PublicRouteTable"
        },
        "DestinationCidrBlock": "0.0.0.0/0",
        "GatewayId": {
          "Ref": "InternetGateway"
        }
      }
    },
    "PublicSubnetRouteTableAssociation1": {
      "Type": "AWS::EC2::SubnetRouteTableAssociation",
      "Properties": {
        "SubnetId": {
          "Ref": "PublicSubnet1"
        },
        "RouteTableId": {
          "Ref": "PublicRouteTable"
        }
      }
    },
    "PublicNetworkAcl": {
      "Type": "AWS::EC2::NetworkAcl",
      "Properties": {
        "VpcId": {
          "Ref": "VPC"
        },
        "Tags": [
          {
            "Key": "Application",
            "Value": {
              "Ref": "AWS::StackName"
            }
          },
          {
            "Key": "Network",
            "Value": "Public"
          }
        ]
      }
    },
    "InboundHTTPPublicNetworkAclEntry": {
      "Type": "AWS::EC2::NetworkAclEntry",
      "Properties": {
        "NetworkAclId": {
          "Ref": "PublicNetworkAcl"
        },
        "RuleNumber": "100",
        "Protocol": "6",
        "RuleAction": "allow",
        "Egress": "false",
        "CidrBlock": "0.0.0.0/0",
        "PortRange": {
          "From": "80",
          "To": "80"
        }
      }
    },
    "InboundHTTPSPublicNetworkAclEntry": {
      "Type": "AWS::EC2::NetworkAclEntry",
      "Properties": {
        "NetworkAclId": {
          "Ref": "PublicNetworkAcl"
        },
        "RuleNumber": "101",
        "Protocol": "6",
        "RuleAction": "allow",
        "Egress": "false",
        "CidrBlock": "0.0.0.0/0",
        "PortRange": {
          "From": "443",
          "To": "443"
        }
      }
    },
    "InboundSSHPublicNetworkAclEntry": {
      "Type": "AWS::EC2::NetworkAclEntry",
      "Properties": {
        "NetworkAclId": {
          "Ref": "PublicNetworkAcl"
        },
        "RuleNumber": "102",
        "Protocol": "6",
        "RuleAction": "allow",
        "Egress": "false",
        "CidrBlock": "0.0.0.0/0",
        "PortRange": {
          "From": "22",
          "To": "22"
        }
      }
    },
    "InboundEmphemeralPublicNetworkAclEntry": {
      "Type": "AWS::EC2::NetworkAclEntry",
      "Properties": {
        "NetworkAclId": {
          "Ref": "PublicNetworkAcl"
        },
        "RuleNumber": "103",
        "Protocol": "6",
        "RuleAction": "allow",
        "Egress": "false",
        "CidrBlock": "0.0.0.0/0",
        "PortRange": {
          "From": "1024",
          "To": "65535"
        }
      }
    },
    "OutboundPublicNetworkAclEntry": {
      "Type": "AWS::EC2::NetworkAclEntry",
      "Properties": {
        "NetworkAclId": {
          "Ref": "PublicNetworkAcl"
        },
        "RuleNumber": "100",
        "Protocol": "6",
        "RuleAction": "allow",
        "Egress": "true",
        "CidrBlock": "0.0.0.0/0",
        "PortRange": {
          "From": "0",
          "To": "65535"
        }
      }
    },
    "PublicSubnetNetworkAclAssociation1": {
      "Type": "AWS::EC2::SubnetNetworkAclAssociation",
      "Properties": {
        "SubnetId": {
          "Ref": "PublicSubnet1"
        },
        "NetworkAclId": {
          "Ref": "PublicNetworkAcl"
        }
      }
    },
    "EC2SecurityGroup": {
      "Type": "AWS::EC2::SecurityGroup",
      "Properties": {
        "GroupDescription": "Enable access to the EC2 host",
        "VpcId": {
          "Ref": "VPC"
        },
        "SecurityGroupIngress": [
          {
            "IpProtocol": "-1",
            "FromPort": "-1",
            "ToPort": "-1",
            "CidrIp": "0.0.0.0/0"
          }
        ]
      }
    },
    "SGBaseIngress": {
      "Type": "AWS::EC2::SecurityGroupIngress",
      "Properties": {
        "GroupId": {
          "Ref": "EC2SecurityGroup"
        },
        "IpProtocol": "tcp",
        "FromPort": "80",
        "ToPort": "80",
        "SourceSecurityGroupId": {
          "Ref": "EC2SecurityGroup"
        }
      }
    },
    "Workstation": {
      "Type": "AWS::EC2::Instance",
      "Properties": {
        "InstanceType": "t3.small",
        "UserData": {
          "Fn::Base64": {
            "Fn::Join": [
              "",
              [
                "#!/bin/bash -xe\n",
                "/bin/echo '%password%' | /bin/passwd cloud_user --stdin\n",
                "/usr/sbin/setenforce 0\n",
                "/usr/bin/systemctl stop firewalld\n",
                "export PYTHONPATH=\"${PYTHONPATH}:/usr/local/lib/python2.7/site-packages/\"\n",

                "cd /home/cloud_user\n",

                "git init\n",
                "git remote add origin https://github.com/linuxacademy/content-using-pythons-maths-science-and-engineering-libraries.git\n",
                "git pull --depth=1 origin math-lab-1\n",
                "rm -rf /home/cloud_user/.git\n",
                
                "echo 3.8.2 > /home/cloud_user/.python-version\n",

                "chown cloud_user:cloud_user -R /home/cloud_user\n",

                "/opt/aws/bin/cfn-signal -e $? ",
                "         --stack ",
                {
                  "Ref": "AWS::StackName"
                },
                "         --resource Workstation ",
                "         --region ",
                {
                  "Ref": "AWS::Region"
                },
                "\n"
              ]
            ]
          }
        },
        "ImageId": "%ami-204%",
        "NetworkInterfaces": [
          {
            "GroupSet": [
              {
                "Ref": "EC2SecurityGroup"
              }
            ],
            "AssociatePublicIpAddress": "true",
            "DeviceIndex": "0",
            "DeleteOnTermination": "true",
            "SubnetId": {
              "Ref": "PublicSubnet1"
            }
          }
        ]
      },
      "CreationPolicy": {
        "ResourceSignal": {
          "Count": "1",
          "Timeout": "PT10M"
        }
      }
    }
  },
  "Outputs": {
    "pubIpAddress1": {
      "Description": "Public IP address of Workstation",
      "Value": {
        "Fn::GetAtt": ["Workstation", "PublicIp"]
      }
    },
    "privIpAddress1": {
      "Description": "Private IP address of Workstation",
      "Value": {
        "Fn::GetAtt": ["Workstation", "PrivateIp"]
      }
    }
  }
}
```

## Videos and Guide

## Lab Guide